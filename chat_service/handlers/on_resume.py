import chainlit as cl
from ai.image_chain import ImageChain
from chainlit.types import ThreadDict


async def execute(thread: ThreadDict):
    user_history = []
    root_messages = [m for m in thread['steps'] if m['parentId'] is None]
    for message in root_messages:
        # Update message history
        if message['type'] == 'user_message':
            user_history.append(message['output'])

    cl.user_session.set('user_history', user_history)
    cl.user_session.set('chain', ImageChain())
