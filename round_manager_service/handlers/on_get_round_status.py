from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    status = round_state.get_round_status()
    logger.info(f'Round status: {status}')

    return JSONResponse(content={'status': status})
