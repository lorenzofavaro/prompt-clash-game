from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    time_remaining_formatted = round_state.get_round_time_remaining_formatted()
    logger.info(f'Round time remaining: {time_remaining_formatted}')

    return JSONResponse(content={'time_remaining_formatted': time_remaining_formatted})
