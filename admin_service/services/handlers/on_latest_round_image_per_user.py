from fastapi.responses import JSONResponse
from services.combined_service import combined_service
from utils.logger import logger
from utils.time_utils import convert_to_non_utc_time


async def execute():
    try:
        data, status_code = await combined_service.latest_image_per_user()
        if status_code == 200 and isinstance(data, list):
            for image_dict in data:
                image_dict['createdAt'] = convert_to_non_utc_time(image_dict['createdAt'])
            logger.info(f'Found {len(data)} images')
        else:
            logger.error(f'Failed to get latest round image per user: {data}')
        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(
            f'Failed to get latest round image per user: {str(e)}', exc_info=True
        )
        return JSONResponse(status_code=500, content={'error': str(e)})
