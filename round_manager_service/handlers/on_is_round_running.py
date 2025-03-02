from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    is_running = round_state.is_round_running()
    logger.info(f'Round is running: {is_running}')

    return JSONResponse(content={'is_round_running': is_running})
