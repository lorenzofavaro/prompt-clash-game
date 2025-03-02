from fastapi.responses import JSONResponse
from models.round_settings import RoundSettings
from services.round_service import round_service
from utils.logger import logger


async def execute(minutes: int, seconds: int, theme: str):
    try:
        settings = RoundSettings(minutes=minutes, seconds=seconds, theme=theme)
        data, status_code = await round_service.save_settings(
            minutes=settings.minutes, seconds=settings.seconds, theme=settings.theme
        )
        logger.info(f'Settings saved successfully with status code {status_code}')
        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to save settings: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
