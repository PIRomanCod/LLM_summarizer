from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    chat_input = Column(String, nullable=True)
    chat_output = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
