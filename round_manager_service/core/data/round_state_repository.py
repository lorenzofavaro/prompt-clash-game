from config import config
from pymysql.err import OperationalError as PyMySQLOperationalError
from sqlalchemy import Column
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential

Base = declarative_base()


class RoundStateModel(Base):
    __tablename__ = 'rounds'

    id = Column(Integer, primary_key=True)
    theme = Column(String, nullable=False)
    start_timestamp = Column(TIMESTAMP, nullable=False)
    end_timestamp = Column(TIMESTAMP, nullable=True)
    time_duration = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'theme': self.theme,
            'start_timestamp': self.start_timestamp.isoformat()
            if self.start_timestamp
            else None,
            'end_timestamp': self.end_timestamp.isoformat()
            if self.end_timestamp
            else None,
            'time_duration': self.time_duration,
        }


class ThemeModel(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }


class RoundStateRepository:
    _instance = None
    _engine = None
    _session = None

    @classmethod
    async def initialize(cls):
        if not cls._instance:
            cls._instance = cls()
            cls._engine = create_async_engine(
                f'mysql+aiomysql://{config.mysql_user}:{config.mysql_password}'
                f'@{config.mysql_host}:{config.mysql_port}/{config.mysql_db}'
            )
            cls._session = sessionmaker(
                cls._engine, expire_on_commit=False, class_=AsyncSession
            )
        return cls._instance

    @classmethod
    async def get_session(cls):
        if not cls._instance:
            await cls.initialize()
        return cls._session()

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        retry=retry_if_exception_type((OperationalError, PyMySQLOperationalError)),
    )
    async def insert_round_state(round_state):
        async with await RoundStateRepository.get_session() as session:
            round_state_model = RoundStateModel(
                theme=round_state.get_round_theme(),
                start_timestamp=round_state.get_round_start_timestamp(),
                end_timestamp=round_state.get_round_end_timestamp(),
                time_duration=round_state.get_round_time_duration(),
            )
            session.add(round_state_model)
            await session.commit()

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        retry=retry_if_exception_type((OperationalError, PyMySQLOperationalError)),
    )
    async def get_last_round():
        async with await RoundStateRepository.get_session() as session:
            result = await session.execute(
                select(RoundStateModel).order_by(RoundStateModel.id.desc())
            )
            last_round = result.scalars().first()
            return last_round

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        retry=retry_if_exception_type((OperationalError, PyMySQLOperationalError)),
    )
    async def get_round_count():
        async with await RoundStateRepository.get_session() as session:
            result = await session.execute(
                select(func.count()).select_from(RoundStateModel)
            )
            return result.scalar()

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        retry=retry_if_exception_type((OperationalError, PyMySQLOperationalError)),
    )
    async def get_last_n_rounds(n: int):
        async with await RoundStateRepository.get_session() as session:
            result = await session.execute(
                select(RoundStateModel).order_by(RoundStateModel.id.desc()).limit(n)
            )
            return result.scalars().all()

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        retry=retry_if_exception_type((OperationalError, PyMySQLOperationalError)),
    )
    async def get_themes():
        async with await RoundStateRepository.get_session() as session:
            result = await session.execute(select(ThemeModel))
            return result.scalars().all()
