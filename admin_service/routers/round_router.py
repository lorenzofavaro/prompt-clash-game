from fastapi import APIRouter
from models.round_settings import RoundSettings
from services.handlers import on_pause_round
from services.handlers import on_save_settings
from services.handlers import on_start_round
from services.handlers import on_stop_round

router = APIRouter(prefix='/api/round')


@router.post('/save_settings')
async def save_settings(settings: RoundSettings):
    return await on_save_settings.execute(
        settings.minutes, settings.seconds, settings.theme
    )


@router.post('/start')
async def start():
    return await on_start_round.execute()


@router.post('/pause')
async def pause():
    return await on_pause_round.execute()


@router.post('/stop')
async def stop():
    return await on_stop_round.execute()
