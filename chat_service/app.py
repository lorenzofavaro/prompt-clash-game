from chainlit.utils import mount_chainlit
from fastapi import FastAPI
from routers.chat_router import router as chat_router
from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(chat_router)

path = '/' if os.getenv('ENVIRONMENT') == 'dev' else '/chat/'
mount_chainlit(app=app, target='cl_app.py', path=path)
