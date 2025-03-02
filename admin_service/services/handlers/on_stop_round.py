from fastapi.responses import JSONResponse
from services.round_service import round_service
from utils.logger import logger


async def execute():
    try:
        data, status_code = await round_service.stop()
        logger.info(f'Round stopped successfully with status code {status_code}')

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to stop round: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
