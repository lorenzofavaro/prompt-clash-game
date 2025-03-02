from typing import Any
from typing import Dict

from config import config
from services.http_client import HTTPClient
from utils.time_utils import minutes_and_seconds_to_seconds


class RoundService:
    def __init__(self):
        self.base_url = config.round_service_endpoint

    async def start(self) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/start')

    async def pause(self) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/pause')

    async def stop(self) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            return await client.post('/stop')

    async def save_settings(
        self, minutes: int, seconds: int, theme: str
    ) -> Dict[str, Any]:
        async with HTTPClient(self.base_url) as client:
            round_duration = minutes_and_seconds_to_seconds(minutes, seconds)

            duration_response, duration_status_code = await client.post(
                f'/set_duration?duration={round_duration}'
            )
            theme_response, theme_status_code = await client.post(
                f'/set_theme?theme={theme}'
            )

            return [duration_response, theme_response], max(
                duration_status_code, theme_status_code
            )


round_service = RoundService()
