from typing import Any
from typing import Optional
from typing import Tuple

import httpx
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential
from utils.logger import logger


class HTTPClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=timeout)
        self.logger = logger

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((httpx.RequestError, ConnectionError)),
    )
    async def _make_request(
        self, method: str, endpoint: str, **kwargs
    ) -> httpx.Response:
        url = f'{self.base_url}{endpoint}'
        self.logger.info(f'Making {method} request to {url}')
        try:
            response = await self.client.request(method, url, **kwargs)
            self.logger.info(f'Response status code: {response.status_code}')
            return response
        except Exception as e:
            self.logger.error(f'Request failed: {str(e)}')
            raise

    async def get(
        self, endpoint: str, params: Optional[dict] = None
    ) -> Tuple[Any, int]:
        response = await self._make_request('GET', endpoint, params=params)
        return response.json(), response.status_code

    async def post(self, endpoint: str, data: Optional[dict] = None) -> Tuple[Any, int]:
        response = await self._make_request('POST', endpoint, json=data)
        return response.json(), response.status_code
