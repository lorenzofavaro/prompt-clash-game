from fastapi import WebSocket
from utils.logger import logger


class SocketManager:
    """Class defining socket events"""

    def __init__(self):
        """init method, keeping track of connections"""
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        """connect event"""
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f'New connection added. Total connections: {len(self.active_connections)}')

    async def disconnect(self, websocket: WebSocket):
        """disconnect event"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f'Connection removed. Total connections: {len(self.active_connections)}')

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Direct Message"""
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        """Broadcast message to all connected clients"""
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.warning(f'Failed to send message to connection: {str(e)}')
                disconnected.append(connection)

        for conn in disconnected:
            await self.disconnect(conn)
