from core.data.round_state_repository import RoundStateRepository
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute():
    last_round = await RoundStateRepository.get_last_round()
    if last_round:
        logger.info(f'Last round: {last_round.to_dict()}')
        return JSONResponse(content={'round': last_round.to_dict()})

    logger.info('No rounds found.')
    return JSONResponse(content={'message': 'No rounds found.'})
