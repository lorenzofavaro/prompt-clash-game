from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.connection_manager import ConnectionManager
from collections import defaultdict

router = APIRouter(prefix='/api/chat')


@router.get('/count_images')
async def count_images():
    try:
        connection_manager = ConnectionManager()
        data_layer = connection_manager.get_data_layer()
        response = await data_layer.get_count_images()
        return JSONResponse(content=response)
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)


@router.get('/latest_round_image_per_user')
async def latest_round_image_per_user(start_timestamp: str, end_timestamp: str):
    try:
        connection_manager = ConnectionManager()
        data_layer = connection_manager.get_data_layer()
        response = await data_layer.get_latest_round_image_per_user(
            start_timestamp, end_timestamp
        )
        return JSONResponse(content=response)
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)


@router.get('/get_round_images')
async def get_round_images(start_timestamp: str, end_timestamp: str):
    try:
        connection_manager = ConnectionManager()
        data_layer = connection_manager.get_data_layer()
        response = await data_layer.get_round_images(start_timestamp, end_timestamp)

        transformed_response = defaultdict(list)
        for item in response:
            transformed_response[item['identifier']].append({
                'url': item['url'],
                'createdAt': item['createdAt']
            })

        return JSONResponse(content=dict(transformed_response))
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)
