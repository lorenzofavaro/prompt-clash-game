from pydantic import BaseModel
from pydantic import Field


class Round(BaseModel):
    theme: str = Field(min_length=1)
    start_timestamp: str = Field(min_length=1)
    end_timestamp: str = Field(min_length=1)
    time_duration: int = Field(ge=0)
