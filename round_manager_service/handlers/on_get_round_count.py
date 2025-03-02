from core.data.round_state_repository import RoundStateRepository
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute():
    count = await RoundStateRepository.get_round_count()
    logger.info(f'Round count: {count}')

    return JSONResponse(content={'rounds_count': count})
