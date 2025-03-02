from typing import Any
from typing import Dict
from typing import List

from api.http_client import HTTPClient
from config import config


class AdminAPI:
    def __init__(self):
        self.base_url = config.admin_service.base_url

    async def get_rounds_count(self) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/api/rounds/count')

    async def get_last_n_rounds(self, n: int) -> List[Dict[str, int]]:
        async with HTTPClient(self.base_url) as client:
            return await client.get(f'/api/rounds/last/{n}')

    async def start_round(self) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/api/round/start')

    async def pause_round(self) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/api/round/pause')

    async def stop_round(self) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/api/round/stop')

    async def save_settings(self, settings: Dict[str, int]) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/api/round/save_settings', data=settings)

    async def get_images_count(self) -> Dict[str, int]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/api/chat/count_images')

    async def latest_round_image_per_user(self) -> List[Dict[str, int]]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/api/chat/latest_round_image_per_user')

    async def get_all_themes(self) -> List[Dict[str, Any]]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/api/themes/all')


admin_api = AdminAPI()
