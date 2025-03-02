from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(theme: str, round_state: RoundState):
    try:
        round_state.set_round_theme(theme)
        logger.info(f"Theme set to '{theme}'.")

        return JSONResponse(content={'message': f"Theme set to '{theme}'."})
    except ValueError as e:
        logger.error(f'Failed to set theme: {str(e)}', exc_info=True)
        return JSONResponse(content={'message': str(e)}, status_code=400)
