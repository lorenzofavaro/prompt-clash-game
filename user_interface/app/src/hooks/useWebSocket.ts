import { useEffect, useState } from 'react';
import config from '@/config/config';
import { checkHealth } from '@/api/health';

const useWebSocket = () => {
  const [data, setData] = useState<{ theme?: string; time_remaining?: string; status?: string }>({});
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const [isHealthy, setIsHealthy] = useState(false);

  useEffect(() => {
    let timeoutId: NodeJS.Timeout;

    const checkServiceHealth = async () => {
      const healthy = await checkHealth();
      setIsHealthy(healthy);

      if (!healthy) {
        timeoutId = setTimeout(checkServiceHealth, 1000);
      }
    };

    if (!isHealthy) {
    checkServiceHealth();
    }

    return () => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
    };
  }, [isHealthy]);

  useEffect(() => {
    if (!isHealthy) {
      if (socket) {
        socket.close();
        setSocket(null);
      }
      return;
    }

    if (socket?.readyState === WebSocket.OPEN) {
      return;
    }

    const connectWebSocket = () => {
      const devServer = config.devRoundWebSocketBaseUrl;
      const url = import.meta.env.DEV
        ? devServer
        : window.origin.replace(/^http(s?):\/\//, 'ws$1://');

      const finalUrl = url + '/api/round/ws';
      const ws = new WebSocket(finalUrl);

      ws.onopen = () => {
        console.log("WebSocket connection established");
      };

      ws.onmessage = (event) => {
        const receivedData = JSON.parse(event.data);
        // console.log("receivedData", receivedData);
        setData(receivedData);
      };

      ws.onerror = (error) => {
        console.error("WebSocket error observed:", error);
        setIsHealthy(false);
      };

      ws.onclose = (event) => {
        console.log("WebSocket connection closed:", event);
        setIsHealthy(false);
      };

      setSocket(ws);
    };

    connectWebSocket();

    return () => {
      if (socket) {
        socket.close();
      }
    };
  }, [isHealthy]);

  return { data, socket, isHealthy };
};

export default useWebSocket;
