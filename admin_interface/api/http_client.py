from typing import Optional

import httpx
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential
from utils.logger import logger


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((httpx.RequestError, ConnectionError)),
        before_sleep=lambda retry_state: logger.warning(
            f'Retrying request after attempt {retry_state.attempt_number} due to: {retry_state.outcome.exception()}'
        ),
    )
    async def _make_request(
        self, method: str, endpoint: str, **kwargs
    ) -> httpx.Response:
        url = f'{self.base_url}{endpoint}'
        logger.debug(f'Making {method} request to {url}')
        try:
            response = await self.client.request(method, url, **kwargs)
            logger.debug(f'Response status code: {response.status_code}')
            return response
        except Exception as e:
            logger.error(f'Request failed: {str(e)}')
            raise

    async def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        logger.debug(f'GET request to {endpoint} with params: {params}')
        response = await self._make_request('GET', endpoint, params=params)
        return response.json(), response.status_code

    async def post(self, endpoint: str, data: Optional[dict] = None) -> dict:
        logger.debug(f'POST request to {endpoint} with data: {data}')
        response = await self._make_request('POST', endpoint, json=data)
        return response.json(), response.status_code
