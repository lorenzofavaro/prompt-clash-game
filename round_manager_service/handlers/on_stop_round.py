from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    try:
        await round_state.stop_round()
        logger.info('Round stopped successfully')

        return JSONResponse(content={'message': 'Round stopped.'})
    except ValueError as e:
        logger.error(f'Failed to stop round: {str(e)}', exc_info=True)
        return JSONResponse(content={'message': str(e)}, status_code=400)
