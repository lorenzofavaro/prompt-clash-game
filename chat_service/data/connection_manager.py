from typing import Optional
from data.mysql_data_layer import MySQLDataLayer
from data.oci_storage_client import OCIStorageClient
from config import config
from utils.logger import logger
from tenacity import retry, stop_after_attempt, wait_exponential


class ConnectionManager:
    _instance: Optional['ConnectionManager'] = None
    _data_layer: Optional[MySQLDataLayer] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._initialize_connections()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    def _initialize_connections(self):
        try:
            self._create_data_layer()
        except Exception as e:
            logger.error(f'Error initializing connections: {e}')
            self.cleanup()
            raise

    def _create_data_layer(self):
        storage_client = OCIStorageClient(
            bucket=config.oci_bucket_name,
            region_name=config.oci_region_name,
            aws_access_key_id=config.oci_access_key_id,
            aws_secret_access_key=config.oci_secret_access_key,
            endpoint_url=config.oci_endpoint_url,
        )

        self._data_layer = MySQLDataLayer(
            conninfo=f'mysql+aiomysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}/{config.mysql_db}',
            storage_provider=storage_client,
        )

    def get_data_layer(self) -> MySQLDataLayer:
        self._initialize_connections()
        return self._data_layer

    def cleanup(self):
        self._data_layer = None
