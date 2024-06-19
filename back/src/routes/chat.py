from fastapi import APIRouter, HTTPException, Depends, status, Query, Request
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas.chat import ChatBase, ChatResponse
from src.repository import chat as repository_chats


router = APIRouter(prefix='/summarize', tags=["chats"])


@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def summarize(body: ChatBase, db: Session = Depends(get_db)):
    """
    The **summarize** function creates a summary of given text.

    :param db: Session: Pass the database session to the repository layer
    :return: summary of input, which serialized as json
    """
    summary = await repository_chats.create_chat(body, db)
    return summary
