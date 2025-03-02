import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv(f'{os.getcwd()}/.env')


@dataclass
class Config:
    max_query_length: int = 2000

    user1_pass: str = os.getenv('USER1_PASS')
    user2_pass: str = os.getenv('USER2_PASS')
    user3_pass: str = os.getenv('USER3_PASS')
    user4_pass: str = os.getenv('USER4_PASS')
    user5_pass: str = os.getenv('USER5_PASS')

    mysql_user: str = os.getenv('MYSQL_USER')
    mysql_password: str = os.getenv('MYSQL_PASSWORD')
    mysql_db: str = os.getenv('MYSQL_DB')
    mysql_host: str = os.getenv('MYSQL_HOST')
    mysql_port: int = int(os.getenv('MYSQL_PORT'))

    oci_secret_access_key: str = os.getenv('OCI_SECRET_ACCESS_KEY')
    oci_access_key_id: str = os.getenv('OCI_ACCESS_KEY_ID')
    oci_endpoint_url: str = os.getenv('OCI_ENDPOINT_URL')
    oci_bucket_name: str = os.getenv('OCI_BUCKET_NAME')
    oci_region_name: str = os.getenv('OCI_REGION_NAME')


config = Config()
