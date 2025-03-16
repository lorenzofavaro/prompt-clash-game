import asyncio
import time
from utils.logger import logger

import chainlit as cl
from config import Config


@cl.step(type='tool', name='Message Length Check', show_input=False)
async def message_length_step(max_query_length: int):
    return f'The input was truncated to {max_query_length} characters.'


async def execute(message: cl.Message, user_session, config: Config):
    start_time = time.time()
    user_id = message.author or 'anonymous'

    async def respond(user_history: str, question: str):
        gen_start_time = time.time()
        user_history_str = '\n\n'.join(user_history)
        msg = cl.Message(content='Prompt used: ')
        await msg.send()

        input_args = {'user_history': user_history_str, 'image_desc': question}

        prompt_time = time.time()
        async for response in chain.ainvoke(input_args):
            generation_prompt_token = response.get('generation_prompt_token', None)
            image_url = response.get('image_url', None)
            exception = response.get('exception', None)

            if exception:
                msg.content = exception
                await msg.update()
                logger.error(f'Image generation failed: {exception}')
                break
            elif image_url:
                image_gen_time = time.time() - prompt_time
                logger.info(f'Image generation took {image_gen_time:.2f}s for user {user_id}')
                image = cl.Image(name='Generated image', url=image_url)
                msg.elements = [image]
                await msg.update()
            else:
                await msg.stream_token(token=generation_prompt_token)

        total_time = time.time() - gen_start_time
        logger.info(f'Total response time: {total_time:.2f}s for user {user_id}')

    user_history = user_session.get('user_history')
    chain: Runnable = user_session.get('chain')
    question: str = message.content

    # Check if the message is too long
    if len(message.content) > config.max_query_length:
        question = message.content[: config.max_query_length]
        await message_length_step(config.max_query_length)

    # Update user history
    user_history.append(question)

    asyncio.create_task(respond(user_history, question))
    processing_time = time.time() - start_time
    logger.info(f'Message processing setup took {processing_time:.2f}s for user {user_id}')
