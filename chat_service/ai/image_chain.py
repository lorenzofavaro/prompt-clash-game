from ai.prompts import system_prompt
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.prompts.prompt import PromptTemplate
from utils.logger import logger
from typing import AsyncGenerator
from . import llm
import asyncio
from openai import BadRequestError


class ImageChain:
    def __init__(self):
        self.prompt_template = PromptTemplate(
            input_variables=['user_history', 'image_desc'], template=system_prompt
        )
        self.chain = self.prompt_template | llm

    def invoke(self, request: dict) -> dict:
        response = self.chain.invoke(request)
        generation_prompt = response.content
        logger.info(f'Generated prompt: {generation_prompt}')

        image_url = DallEAPIWrapper(model='dall-e-3').run(generation_prompt)

        response = {'generation_prompt': generation_prompt, 'image_url': image_url}
        return response


    async def ainvoke(self, request: dict) -> AsyncGenerator[dict, None]:
        generation_prompt = ''
        async for response in self._stream_generation_prompt(request):
            yield {'generation_prompt_token': response['content']}
            if response['type'] == 'text':
                generation_prompt += response['content']

        logger.info(f'Generated prompt: {generation_prompt}')

        try:
            image_url = await self._generate_image(generation_prompt)
            yield {'image_url': image_url}
        except ValueError as e:
            logger.error(f'Image generation failed: {str(e)}')
            yield {'exception': str(e)}
        except Exception as e:
            logger.error(f'Unexpected error during image generation: {str(e)}')
            yield {'exception': "⚠️ An unexpected error occurred during image generation. ⚠️\nPlease try again."}


    async def _generate_image(self, generation_prompt: str) -> str:
        try:
            image_url = await asyncio.to_thread(
                DallEAPIWrapper(model='dall-e-3').run,
                generation_prompt
            )
            return image_url
        except BadRequestError as e:
            if 'content_policy_violation' in str(e):
                logger.warning(f'Content policy violation in prompt: {generation_prompt}')
                raise ValueError('⚠️ The generated prompt violates content policy. ⚠️\nPlease try again with a different description.')
            raise e


    async def _stream_generation_prompt(self, request: dict) -> AsyncGenerator[dict, None]:
        async for event in self.chain.astream_events(request, version='v2'):
            if event['event'] == 'on_chat_model_start' or event['event'] == 'on_chat_model_end':
                response = {'type': 'format', 'content': '**'}
                yield response
            elif event['event'] == 'on_chat_model_stream':
                content = event['data']['chunk'].content or ''
                response = {'type': 'text', 'content': content}
                yield response
