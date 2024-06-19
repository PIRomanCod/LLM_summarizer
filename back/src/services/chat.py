from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline


async def llm_summarizer(chat_input: str) -> str:
    """
    implementation of summarization task with langchain and HuggingFace

    :param chat_input: The long text to be summarized.
    :type chat_input: str
    :return: The summary of the long text.
    """
    summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)

    summary = summarizer(chat_input)
    return summary
