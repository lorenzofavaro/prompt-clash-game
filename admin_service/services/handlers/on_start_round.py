from fastapi.responses import JSONResponse
from services.round_service import round_service
from utils.logger import logger


async def execute():
    try:
        data, status_code = await round_service.start()
        logger.info(f'Round started successfully with status code {status_code}')

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to start round: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
