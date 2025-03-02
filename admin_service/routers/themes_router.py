from fastapi import APIRouter
from services.handlers import on_all_themes

router = APIRouter(prefix='/api/themes')


@router.get('/all')
async def get_all_themes():
    return await on_all_themes.execute()
