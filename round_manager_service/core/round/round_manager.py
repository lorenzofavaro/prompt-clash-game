from core.round.round_state import RoundState
from core.streaming.socket_manager import SocketManager
from fastapi import APIRouter
from fastapi import WebSocket
from handlers import on_get_last_n_rounds
from handlers import on_get_last_round
from handlers import on_get_round_count
from handlers import on_get_round_status
from handlers import on_get_round_theme
from handlers import on_get_round_time_remaining
from handlers import on_is_round_running
from handlers import on_pause_round
from handlers import on_set_round_theme
from handlers import on_set_round_time_duration
from handlers import on_socket
from handlers import on_start_round
from handlers import on_stop_round
from handlers import on_get_all_themes


class RoundManager:
    def __init__(self):
        self.manager = SocketManager()
        self.round_state = RoundState()

        self.router = APIRouter(prefix='/api')
        self._configure_router()

        self.round_router = APIRouter(prefix='/api/round')
        self._configure_round_router()

        self.rounds_router = APIRouter(prefix='/api/rounds')
        self._configure_rounds_router()

        self.themes_router = APIRouter(prefix='/api/themes')
        self._configure_themes_router()

    def _configure_router(self):
        @self.router.get('/health')
        async def get_health():
            return {'message': 'Round Manager Service is running'}

    def _configure_round_router(self):
        @self.round_router.post('/set_theme')
        async def set_theme(theme: str):
            return await on_set_round_theme.execute(theme, self.round_state)

        @self.round_router.post('/set_duration')
        async def set_round_duration(duration: int):
            return await on_set_round_time_duration.execute(duration, self.round_state)

        @self.round_router.post('/start')
        async def start_round():
            return await on_start_round.execute(self.round_state)

        @self.round_router.post('/pause')
        async def pause_round():
            return await on_pause_round.execute(self.round_state)

        @self.round_router.post('/stop')
        async def stop_round():
            return await on_stop_round.execute(self.round_state)

        @self.round_router.get('/theme')
        async def get_round_theme():
            return await on_get_round_theme.execute(self.round_state)

        @self.round_router.get('/is_running')
        async def is_round_running():
            return await on_is_round_running.execute(self.round_state)

        @self.round_router.get('/time_remaining')
        async def get_round_time_remaining():
            return await on_get_round_time_remaining.execute(self.round_state)

        @self.round_router.get('/status')
        async def get_round_status():
            return await on_get_round_status.execute(self.round_state)

        @self.round_router.websocket('/ws')
        async def websocket_endpoint(websocket: WebSocket):
            return await on_socket.execute(self.round_state, self.manager, websocket)

    def _configure_rounds_router(self):
        @self.rounds_router.get('/last')
        async def get_last_round():
            return await on_get_last_round.execute()

        @self.rounds_router.get('/count')
        async def get_round_count():
            return await on_get_round_count.execute()

        @self.rounds_router.get('/last/{n}')
        async def get_last_n_rounds(n: int):
            return await on_get_last_n_rounds.execute(n)

    def _configure_themes_router(self):
        @self.themes_router.get('/all')
        async def get_all_themes():
            return await on_get_all_themes.execute()

    def get_router(self):
        return self.router

    def get_round_router(self):
        return self.round_router

    def get_rounds_router(self):
        return self.rounds_router

    def get_themes_router(self):
        return self.themes_router
