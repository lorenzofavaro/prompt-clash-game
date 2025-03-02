from core.data.round_state_repository import RoundStateRepository
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute(n: int):
    if n <= 0:
        return JSONResponse(
            content={'message': 'Invalid number of rounds.'}, status_code=400
        )
    elif n > 100:
        return JSONResponse(
            content={'message': 'Number of rounds cannot be greater than 100.'},
            status_code=400,
        )

    if rounds := await RoundStateRepository.get_last_n_rounds(n):
        logger.info(f'Found {len(rounds)} rounds')
        return JSONResponse(content={'rounds': [round.to_dict() for round in rounds]})

    logger.info('No rounds found.')
    return JSONResponse(content={'message': 'No rounds found.'})
