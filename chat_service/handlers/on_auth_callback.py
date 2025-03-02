import chainlit as cl
from config import Config


async def execute(username: str, password: str, config: Config):
    valid_users = {
        'user1': config.user1_pass,
        'user2': config.user2_pass,
        'user3': config.user3_pass,
        'user4': config.user4_pass,
        'user5': config.user5_pass,
    }

    if username in valid_users and password == valid_users[username]:
        return cl.User(
            identifier=username, metadata={'role': 'user', 'provider': 'credentials'}
        )

    return None
