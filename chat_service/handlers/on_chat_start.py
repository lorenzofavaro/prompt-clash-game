import chainlit as cl
from ai.image_chain import ImageChain


async def execute():
    user_history = []
    cl.user_session.set('user_history', user_history)
    cl.user_session.set('chain', ImageChain())
