from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    theme = round_state.get_round_theme()
    logger.info(f'Round theme: {theme}')

    return JSONResponse(content={'theme': theme})
