import os
from dataclasses import dataclass
import yaml
from yaml.loader import SafeLoader
from dotenv import load_dotenv

load_dotenv(f'{os.getcwd()}/.env')

@dataclass
class AdminServiceConfig:
    base_url: str

@dataclass
class Config:
    cookie: dict
    credentials: dict
    services: dict
    admin_service: AdminServiceConfig

    @classmethod
    def load(cls) -> 'Config':
        config_path = 'config.yaml'
        with open(config_path) as file:
            yaml_config = yaml.load(file, Loader=SafeLoader)

        admin_service = AdminServiceConfig(
            base_url=os.getenv('ADMIN_SERVICE_URL', 'http://localhost:8002')
        )
        cookie = yaml_config.get('cookie', {})
        cookie_key = os.getenv('COOKIE_KEY')
        if not cookie_key:
            raise ValueError('COOKIE_KEY environment variable must be set')
        cookie['key'] = cookie_key

        admin_password = os.getenv('ADMIN_PASS')
        if not admin_password:
            raise ValueError('ADMIN_PASS environment variable must be set')

        credentials = yaml_config.get('credentials', {})
        credentials['usernames']['admin']['password'] = admin_password

        return cls(
            cookie=cookie,
            credentials=credentials,
            services=yaml_config.get('services', {}),
            admin_service=admin_service
        )

config = Config.load()
