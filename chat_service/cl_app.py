import chainlit as cl
from chainlit.types import ThreadDict
from config import config
from handlers import on_auth_callback
from handlers import on_chat_start
from handlers import on_data_layer
from handlers import on_message
from handlers import on_resume


@cl.on_chat_start
async def start():
    await on_chat_start.execute()


@cl.on_message
async def message(message: cl.Message):
    await on_message.execute(message, cl.user_session, config)


@cl.on_chat_resume
async def chat_resume(thread: ThreadDict):
    await on_resume.execute(thread)


@cl.password_auth_callback
async def auth_callback(username: str, password: str):
    return await on_auth_callback.execute(username, password, config)


@cl.data_layer
def get_data_layer():
    return on_data_layer.execute()
