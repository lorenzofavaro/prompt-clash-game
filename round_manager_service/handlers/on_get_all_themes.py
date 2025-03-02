from core.data.round_state_repository import RoundStateRepository
from fastapi.responses import JSONResponse
from utils.logger import logger


async def execute():
    themes = await RoundStateRepository.get_themes()
    theme_dicts = [theme.to_dict() for theme in themes]
    logger.info(f'Themes: {theme_dicts}')

    return JSONResponse(content={'themes': theme_dicts})
