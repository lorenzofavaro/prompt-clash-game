from config import config
from sqlalchemy.ext.asyncio import create_async_engine
from utils.logger import logger


class MySQLConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            logger.info('Initializing MySQL connection')
            cls._instance.engine = cls._instance.create_engine()
            logger.info('MySQL connection established successfully')
        return cls._instance

    def create_engine(self):
        connection_string = f'mysql+aiomysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}/{config.mysql_db}'
        logger.debug(f'Creating engine with connection string: {connection_string}')
        return create_async_engine(connection_string)

    def get_engine(self):
        return self.engine
