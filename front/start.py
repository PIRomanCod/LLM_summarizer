import streamlit as st
import asyncio

from htmlTemplates import css
from pages.Summary import run_summary

async def main():
    """
    Endpoint for the frontend app.

    This function configures the Streamlit page, sets up the HTML templates, and runs the summarizing chat application.

    """
    st.set_page_config(page_title="Your own summarizing chat",
                       page_icon="👋")

    st.write(css, unsafe_allow_html=True)
    st.title("Welcome to summarizing chat!")
    st.header("Enjoy AI-powered summarizing chat")
    await run_summary()


if __name__ == '__main__':
    asyncio.run(main())
