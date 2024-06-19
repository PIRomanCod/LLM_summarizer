import streamlit as st

from htmlTemplates import css

from pages.src.summary_service import create_chat


async def run_summary():
    """
    Runs the text summarization process.

    This function displays a user interface to input a long text (maximum 1500 characters),
    processes the text to generate a summary, and displays the summarized output.
    """
    st.write(css, unsafe_allow_html=True)

    st.subheader("Your long text (15000 max, english only)")
    input = st.text_input("Enter: ")
    if st.button("Process"):
        payload = {"chat_input": input}
        st.subheader("Your request: ")
        st.write(input)
        try:
            response = await create_chat(payload)
            if isinstance(response, dict) and "chat_output" in response:
                st.subheader("Summary for you: ")
                st.write(response["chat_output"])
            else:
                st.subheader("Error:")
                st.write("The input was not in the expected language.")
        except Exception as e:
            st.subheader("Error:")
            st.write(f"An error occurred: {str(e)}")
