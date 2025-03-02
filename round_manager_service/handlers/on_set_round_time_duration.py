from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(duration: int, round_state: RoundState):
    try:
        round_state.set_round_time_duration(duration)
        logger.info(f'Round time duration set to {duration} seconds.')

        return JSONResponse(
            content={'message': f'Round time duration set to {duration} seconds.'}
        )
    except ValueError as e:
        logger.error(f'Failed to set round time duration: {str(e)}', exc_info=True)
        return JSONResponse(content={'message': str(e)}, status_code=400)
