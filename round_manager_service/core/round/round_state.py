import asyncio
from datetime import datetime
from datetime import timezone
from enum import Enum

from core.data.round_state_repository import RoundStateRepository


class RoundStatus(Enum):
    NOT_STARTED = 'not started'
    RUNNING = 'running'
    PAUSED = 'paused'


class RoundState:
    def __init__(self):
        self.theme: str = '-'
        self.status: RoundStatus = RoundStatus.NOT_STARTED
        self.start_timestamp: str | None = None
        self.end_timestamp: str | None = None
        self.time_duration: int = 0
        self.time_remaining: int = 0

    def set_round_theme(self, theme: str):
        if self.status != RoundStatus.NOT_STARTED:
            raise ValueError('Round is already running.')
        self.theme = theme

    def set_round_time_duration(self, time_duration: int):
        if self.status != RoundStatus.NOT_STARTED:
            raise ValueError('Round is already running.')
        self.time_duration = time_duration
        self.time_remaining = time_duration

    @staticmethod
    def get_utc_now_timestamp():
        return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    def is_round_not_started(self) -> bool:
        return self.status == RoundStatus.NOT_STARTED

    def is_round_running(self) -> bool:
        return self.status == RoundStatus.RUNNING

    def is_round_paused(self) -> bool:
        return self.status == RoundStatus.PAUSED

    def start_round(self):
        if self.status == RoundStatus.RUNNING:
            raise ValueError('Round is already running.')
        elif self.time_duration == 0:
            raise ValueError('Round time duration is not set.')
        elif self.theme is None:
            raise ValueError('Round theme is not set.')

        if self.status == RoundStatus.NOT_STARTED:
            self.start_timestamp = RoundState.get_utc_now_timestamp()

        self.status = RoundStatus.RUNNING
        asyncio.create_task(self.countdown())

    def pause_round(self):
        if self.status != RoundStatus.RUNNING:
            raise ValueError('Round is not running.')

        self.status = RoundStatus.PAUSED

    async def stop_round(self):
        if self.status not in [RoundStatus.RUNNING, RoundStatus.PAUSED]:
            raise ValueError('Round is not running or paused.')

        self.end_timestamp = RoundState.get_utc_now_timestamp()

        await RoundStateRepository.insert_round_state(self)
        self._reset_round()

    def _reset_round(self):
        self.time_duration = 0
        self.time_remaining = 0
        self.theme = '-'
        self.start_timestamp = None
        self.end_timestamp = None
        self.status = RoundStatus.NOT_STARTED

    async def countdown(self):
        while self.status == RoundStatus.RUNNING and self.time_remaining > 0:
            await asyncio.sleep(1)
            self.time_remaining -= 1

        if self.time_remaining == 0:
            await self.stop_round()

    def get_round_theme(self) -> str:
        return self.theme

    def get_round_time_duration(self) -> int:
        return self.time_duration

    def get_round_status(self) -> str:
        return self.status.value

    def get_round_start_timestamp(self) -> str:
        return self.start_timestamp

    def get_round_end_timestamp(self) -> str:
        return self.end_timestamp

    def get_round_time_remaining_formatted(self) -> str:
        if self.time_remaining > 0:

            hours, remainder = divmod(int(self.time_remaining), 3600)
            minutes, seconds = divmod(remainder, 60)
            if hours > 0:
                return f'{hours}:{minutes:02}:{seconds:02}'
            else:
                return f'{minutes:02}:{seconds:02}'
        return '00:00'
