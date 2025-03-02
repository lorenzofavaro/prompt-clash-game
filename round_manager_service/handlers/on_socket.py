import asyncio
import json

from core.round.round_state import RoundState
from core.streaming.socket_manager import SocketManager
from fastapi import WebSocket
from utils.logger import logger


async def execute(
    round_state: RoundState, manager: SocketManager, websocket: WebSocket
):
    await manager.connect(websocket)
    logger.info('New WebSocket connection established')
    try:
        while True:
            response = {
                'theme': round_state.get_round_theme(),
                'time_remaining': round_state.get_round_time_remaining_formatted(),
                'status': round_state.get_round_status(),
            }
            await manager.broadcast(json.dumps(response))
            await asyncio.sleep(0.5)
    except Exception as e:
        logger.error(f'WebSocket connection error: {str(e)}', exc_info=True)
    finally:
        await manager.disconnect(websocket)
        logger.info('WebSocket connection closed')
