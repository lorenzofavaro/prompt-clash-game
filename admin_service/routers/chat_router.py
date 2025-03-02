from fastapi import APIRouter
from services.handlers import on_count_images
from services.handlers import on_latest_round_image_per_user

router = APIRouter(prefix='/api/chat')


@router.get('/count_images')
async def count_images():
    return await on_count_images.execute()


@router.get('/latest_round_image_per_user')
async def latest_round_image_per_user():
    return await on_latest_round_image_per_user.execute()
