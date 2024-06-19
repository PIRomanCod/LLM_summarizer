from fastapi import FastAPI, status

import uvicorn
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

app = FastAPI()

summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")


async def llm_summarizer(chat_input: str) -> str:
    """
    implementation of summarization task with langchain and HuggingFace

    :param chat_input: The long text to be summarized.
    :type chat_input: str
    :return: The summary of the long text.
    """
    summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)
    summary = summarizer(chat_input)
    return summary


@app.post("/summarize", status_code=status.HTTP_200_OK)
async def summarize(body):
    summary = await llm_summarizer(body.strip().lower())
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
