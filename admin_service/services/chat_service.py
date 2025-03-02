from typing import Any
from typing import Dict

from config import config
from services.http_client import HTTPClient


class ChatService:
    def __init__(self):
        self._client = HTTPClient(config.chat_service_endpoint)

    async def count_images(self) -> Dict[str, Any]:
        return await self._client.get('/count_images')

    async def latest_round_image_per_user(
        self, round_start_timestamp: str, round_end_timestamp: str
    ) -> Dict[str, Any]:
        return await self._client.get(
            f'/latest_round_image_per_user?start_timestamp={round_start_timestamp}&end_timestamp={round_end_timestamp}'
        )


chat_service = ChatService()
