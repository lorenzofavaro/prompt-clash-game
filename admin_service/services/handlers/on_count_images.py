from fastapi.responses import JSONResponse
from services.chat_service import chat_service
from utils.logger import logger


async def execute():
    try:
        data, status_code = await chat_service.count_images()
        logger.info(f'Found {data} images')

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to count images: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
