from typing import Any
from typing import Dict
from typing import Union

import boto3
from chainlit import make_async
from chainlit.data.storage_clients.base import EXPIRY_TIME
from chainlit.data.storage_clients.s3 import S3StorageClient
from chainlit.logger import logger


class OCIStorageClient(S3StorageClient):
    """
    Class to enable Oracle Cloud Infrastructure Object Storage storage provider
    """

    def __init__(self, bucket: str, **kwargs: Any):
        try:
            self.bucket = bucket
            self.client = boto3.client('s3', **kwargs)
            logger.info('OCIStorageClient initialized')
        except Exception as e:
            logger.warn(f'OCIStorageClient initialization error: {e}')

    def sync_get_read_url(self, object_key: str, expires_in: int = EXPIRY_TIME) -> str:
        try:
            url = self.client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket, 'Key': object_key},
                ExpiresIn=expires_in,
            )
            return url
        except Exception as e:
            logger.warn(f'OCIStorageClient, get_read_url error: {e}')
            return object_key

    async def get_read_url(self, object_key: str) -> str:
        return await make_async(self.sync_get_read_url)(object_key)

    def sync_upload_file(
        self,
        object_key: str,
        data: Union[bytes, str],
        mime: str = 'application/octet-stream',
        overwrite: bool = True,
    ) -> Dict[str, Any]:
        try:
            self.client.put_object(
                Bucket=self.bucket, Key=object_key, Body=data, ContentType=mime
            )
            duration = 3600 * 24 * 7  # 1 week
            url = self.sync_get_read_url(object_key, expires_in=duration)
            return {'object_key': object_key, 'url': url}
        except Exception as e:
            logger.warn(f'OCIStorageClient, upload_file error: {e}')
            return {}

    async def upload_file(
        self,
        object_key: str,
        data: Union[bytes, str],
        mime: str = 'application/octet-stream',
        overwrite: bool = True,
    ) -> Dict[str, Any]:
        return await make_async(self.sync_upload_file)(
            object_key, data, mime, overwrite
        )

    def sync_delete_file(self, object_key: str) -> bool:
        try:
            self.client.delete_object(Bucket=self.bucket, Key=object_key)
            return True
        except Exception as e:
            logger.warn(f'OCIStorageClient, delete_file error: {e}')
            return False

    async def delete_file(self, object_key: str) -> bool:
        return await make_async(self.sync_delete_file)(object_key)
