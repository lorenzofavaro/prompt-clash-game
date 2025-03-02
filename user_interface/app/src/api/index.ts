import getRouterBasename from '@/lib/router';
import { toast } from 'sonner';

import { ChainlitAPI, ClientError } from '@chainlit/react-client';
import config from '@/config/config';

const devServer = config.devChatServiceBaseUrl;
const httpEndpoint = import.meta.env.DEV
  ? devServer
  : window.origin + '/chat/';

const on401 = () => {
  if (window.location.pathname !== getRouterBasename() + '/login') {
    // The credentials aren't correct, remove the token and redirect to login
    window.location.href = getRouterBasename() + '/login';
  }
};

const onError = (error: ClientError) => {
  toast.error(error.toString());
};

export const apiClient = new ChainlitAPI(
  httpEndpoint,
  'webapp',
  on401,
  onError
);
