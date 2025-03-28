from fastapi.responses import JSONResponse
from services.rounds_service import rounds_service
from utils.logger import logger


async def execute():
    try:
        data, status_code = await rounds_service.count()
        logger.info(f'Found {data} rounds')

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to count rounds: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
