from typing import Any
from typing import Dict
from typing import List

from config import config
from services.http_client import HTTPClient


class ThemesService:
    def __init__(self):
        self.base_url = config.themes_service_endpoint

    async def get_all(self) -> List[Dict[str, Any]]:
        async with HTTPClient(self.base_url) as client:
            return await client.get('/all')


themes_service = ThemesService()
