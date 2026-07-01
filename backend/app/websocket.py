"""WebSocket configuration for real-time updates"""
from fastapi import WebSocket, WebSocketDisconnect
from typing import Set
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ConnectionManager:
    """Manage WebSocket connections for real-time market data"""
    
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)
        logger.info(f"Client connected. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.discard(websocket)
        logger.info(f"Client disconnected. Total connections: {len(self.active_connections)}")
    
    async def broadcast(self, data: dict):
        if not self.active_connections:
            return
        
        message = json.dumps({
            "type": "market_update",
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        disconnected_clients = []
        
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error sending to client: {str(e)}")
                disconnected_clients.append(connection)
        
        for client in disconnected_clients:
            self.disconnect(client)
    
    async def send_personal(self, websocket: WebSocket, data: dict):
        try:
            message = json.dumps({
                "type": "personal_message",
                "data": data,
                "timestamp": datetime.utcnow().isoformat()
            })
            await websocket.send_text(message)
        except Exception as e:
            logger.error(f"Error sending personal message: {str(e)}")

manager = ConnectionManager()
