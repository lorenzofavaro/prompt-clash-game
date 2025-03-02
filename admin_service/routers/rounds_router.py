from fastapi import APIRouter
from services.handlers import on_count_rounds
from services.handlers import on_last_n_rounds
from services.handlers import on_last_round

router = APIRouter(prefix='/api/rounds')


@router.get('/count')
async def count():
    return await on_count_rounds.execute()


@router.get('/last')
async def last():
    return await on_last_round.execute()


@router.get('/last/{n}')
async def last_n(n: int):
    return await on_last_n_rounds.execute(n)
