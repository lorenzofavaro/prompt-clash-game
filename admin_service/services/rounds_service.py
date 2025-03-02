from typing import Any
from typing import Dict
from typing import List

from config import config
from services.http_client import HTTPClient


class RoundsService:
    def __init__(self):
        self.base_url = config.rounds_service_endpoint

    async def count(self) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/count')

    async def last(self) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/last')

    async def last_n_rounds(self, n: int) -> List[Dict[str, Any]]:
        async with HTTPClient(self.base_url) as client:
            return await client.get(f'/last/{n}')


rounds_service = RoundsService()
