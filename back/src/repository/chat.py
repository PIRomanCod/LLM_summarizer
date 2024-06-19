import os
import pathlib
import re

from sqlalchemy.orm import Session
from src.config.config import settings
from src.database.models import Chat
from src.schemas.chat import ChatBase, ChatResponse
from src.services.chat import llm_summarizer

root_directory = pathlib.Path(__file__).parent.parent.parent.parent
data_folder = settings.data_folder
raw_data = "raw_data"
FULL_PATH = os.path.join(root_directory, data_folder, raw_data)


async def clean_text(text: str) -> str:
    """
    Cleans the input text by removing newline characters and other control characters.

    :param text: The text to be cleaned.
    :type text: str
    :return: The cleaned text.
    """
    cleaned_text = re.sub(r'[\r\n\t]', ' ', text)
    # Optionally, remove any other unwanted characters here
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces with a single space
    cleaned_text = cleaned_text.strip()  # Trim leading and trailing spaces
    return cleaned_text


async def create_chat(body: ChatBase, db: Session) -> ChatResponse:
    """
    The **create_chat** function creates a summary of given text and writes it to the database.

    :param body: ChatBase: Get the given text from the request body
    :param db: Session: Access the database
    :return: A ChatResponse object
    """

    clean_input = await clean_text(body.chat_input)
    chat_output = await summarize(clean_input)

    new_chat = Chat(chat_input=body.chat_input, chat_output=chat_output)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return ChatResponse(
        id=new_chat.id,
        chat_input=new_chat.chat_input,
        chat_output=new_chat.chat_output,
        created_at=new_chat.created_at
    )


async def summarize(text):
    """
    Just transit function yet

    :param text:
    :return summary of long text:
    """
    return await llm_summarizer(text)
