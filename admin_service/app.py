from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.chat_router import router as chat_router
from routers.round_router import router as round_router
from routers.rounds_router import router as rounds_router
from routers.themes_router import router as themes_router
from utils.logger import logger

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

logger.info('Starting admin-service application')

app.include_router(round_router)
app.include_router(rounds_router)
app.include_router(chat_router)
app.include_router(themes_router)

logger.info('All routers have been initialized')
