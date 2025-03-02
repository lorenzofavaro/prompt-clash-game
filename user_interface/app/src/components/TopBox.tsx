import React, { useEffect, useState } from 'react';
import useWebSocket from '@/hooks/useWebSocket'; // Import the custom hook

const TopBox = () => {
  const { data, isHealthy } = useWebSocket(); // Use the custom hook
  const [timeLeft, setTimeLeft] = useState("00:00");
  const [theme, setTheme] = useState("-");

  useEffect(() => {
    // console.log("Received data:", data);
    if (data.theme) {
      setTheme(data.theme);
    }
    if (data.time_remaining) {
      setTimeLeft(data.time_remaining);
    }
  }, [data]);

  if (!isHealthy) {
    return (
      <div className="top-box bg-red-100 mt-4 p-4 rounded-md flex justify-center items-center">
        <div className="text-center">
          <p className="text-l text-red-600">
            <strong>Service unavailable</strong>
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="top-box bg-black-200 mt-4 p-4 rounded-md flex justify-center items-center" key={JSON.stringify(data)}>
      <div className="text-center">
        <p className="text-l">🕒 <strong>{timeLeft}</strong></p>
        <p className="text-l">Theme: <strong>{theme}</strong></p>
      </div>
    </div>
  );
};

export default TopBox;
