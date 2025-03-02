import config from "@/config/config";

export const checkHealth = async () => {
  try {
    const devServer = config.devRoundManagerServiceBaseUrl;
    const url = import.meta.env.DEV
      ? devServer
      : window.origin;

    const finalUrl = url + '/api/health';

    const response = await fetch(finalUrl);
    if (!response.ok) {
      throw new Error('Health check failed');
    }
    return true;
  } catch (error) {
    console.error('Health check error:', error);
    return false;
  }
};
