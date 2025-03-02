from pydantic import BaseModel
from pydantic import Field


class RoundSettings(BaseModel):
    minutes: int = Field(ge=0)
    seconds: int = Field(ge=0, lt=60)
    theme: str = Field(min_length=1)
