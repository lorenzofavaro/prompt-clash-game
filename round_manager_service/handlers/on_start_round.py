from core.round.round_state import RoundState
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(round_state: RoundState):
    try:
        round_state.start_round()
        logger.info('Round started successfully')

        return JSONResponse(
            content={
                'message': 'Round started.',
                'info': {
                    'time_duration': round_state.get_round_time_duration(),
                    'time_remaining': round_state.get_round_time_remaining_formatted(),
                },
            }
        )
    except ValueError as e:
        logger.error(f'Failed to start round: {str(e)}', exc_info=True)
        return JSONResponse(content={'message': str(e)}, status_code=400)
