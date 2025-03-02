import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv(f'{os.getcwd()}/.env')


@dataclass
class Config:
    mysql_user: str = os.getenv('MYSQL_USER')
    mysql_user: str = os.getenv('MYSQL_USER')
    mysql_password: str = os.getenv('MYSQL_PASSWORD')
    mysql_db: str = os.getenv('MYSQL_DB')
    mysql_host: str = os.getenv('MYSQL_HOST')
    mysql_port: int = int(os.getenv('MYSQL_PORT'))


config = Config()
