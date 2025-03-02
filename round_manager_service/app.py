from core.round.round_manager import RoundManager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.logger import logger

app = FastAPI()
logger.info('Starting Round Manager Service')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

round_manager = RoundManager()
router = round_manager.get_router()
round_router = round_manager.get_round_router()
rounds_router = round_manager.get_rounds_router()
themes_router = round_manager.get_themes_router()

app.include_router(router)
app.include_router(round_router)
app.include_router(rounds_router)
app.include_router(themes_router)
logger.info('API routes configured successfully')
