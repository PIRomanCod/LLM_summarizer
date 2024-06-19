import datetime
from typing import Optional

from pydantic import BaseModel, Field

"""
validation for models
"""


class ChatBase(BaseModel):
    chat_input: str = Field(max_length=15000)

    class Config:
        orm_mode = True


class ChatModel(ChatBase):
    # id: int
    created_at: datetime.datetime | None


class ChatResponse(ChatModel):
    chat_output: Optional[str | None]
