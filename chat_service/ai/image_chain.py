from ai.prompts import system_prompt
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.prompts.prompt import PromptTemplate
from utils.logger import logger
from typing import AsyncGenerator
from . import llm
import asyncio


class ImageChain:
    def __init__(self):
        self.prompt_template = PromptTemplate(
            input_variables=['user_history', 'image_desc'], template=system_prompt
        )
        self.chain = self.prompt_template | llm

    def invoke(self, request: dict) -> tuple[str, str]:
        response = self.chain.invoke(request)
        generation_prompt = response.content
        logger.info(f'Generated prompt: {generation_prompt}')

        # Generate the image
        image_url = DallEAPIWrapper(model='dall-e-3').run(generation_prompt)

        return generation_prompt, image_url

    async def ainvoke(self, request: dict) -> AsyncGenerator[tuple[str, str], None]:
        generation_prompt = ''

        async for event in self.chain.astream_events(request, version='v2'):
            if event['event'] == 'on_chat_model_start' or event['event'] == 'on_chat_model_end':
                content = '**'
                yield content, None
            elif event['event'] == 'on_chat_model_stream':
                content = event['data']['chunk'].content or ''
                generation_prompt += content
                yield content, None

        logger.info(f'Generated prompt: {generation_prompt}')

        image_url = await asyncio.to_thread(
            DallEAPIWrapper(model='dall-e-3').run,
            generation_prompt
        )

        # Yield final result with the image URL
        yield None, image_url
