import os
from dataclasses import dataclass


@dataclass
class Config:
    round_service_endpoint: str = os.getenv('ROUND_SERVICE_ENDPOINT', 'http://localhost:8001/api/round')
    rounds_service_endpoint: str = os.getenv('ROUNDS_SERVICE_ENDPOINT', 'http://localhost:8001/api/rounds')
    themes_service_endpoint: str = os.getenv('THEMES_SERVICE_ENDPOINT', 'http://localhost:8001/api/themes')
    chat_service_endpoint: str = os.getenv('CHAT_SERVICE_ENDPOINT', 'http://localhost:8000/api/chat')


config = Config()
