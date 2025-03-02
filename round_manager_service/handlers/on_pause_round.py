from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    try:
        round_state.pause_round()
        logger.info('Round paused successfully')

        return JSONResponse(content={'message': 'Round paused.'})
    except ValueError as e:
        logger.error(f'Failed to pause round: {str(e)}', exc_info=True)
        return JSONResponse(content={'message': str(e)}, status_code=400)
