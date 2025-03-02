from fastapi.responses import JSONResponse
from services.themes_service import themes_service
from utils.logger import logger


async def execute():
    try:
        data, status_code = await themes_service.get_all()
        logger.info(f'Themes: {data}')

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to get themes: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
