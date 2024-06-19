# Summarizing Chat App
Welcome to the Summarizing Chat App! 
This application leverages AI-powered summarization techniques to help users condense long texts into concise summaries. 
Whether you need to summarize articles, documents, or any other lengthy content, our app has you covered.

# Features
- Text Summarization: Input long text and receive a summarized version using state-of-the-art natural language 
  processing techniques.
- User-friendly Interface: Our intuitive user interface makes it easy to input text and view the generated summaries.
- Integration: Seamlessly integrate summarization capabilities into your workflow with our API.
- Persistent Storage: Utilizes PostgreSQL to store user data securely, allowing for retrieval and management of summarized content.
- Streamlit Web App: Built with Streamlit, enabling the creation of a comprehensive and interactive web application for summarization tasks.

# Setup instructions:

- download project from Git
- create poetry env use exist toml
- create in root folder your own .env file like .env.example
- run alembic:
  - alembic init alembic
  - alembic revision --autogenerate -m 'Init'
  - alembic upgrade head


# Run instructions:
- run like full app (from related folder: back/front):
       - uvicorn main:app --host localhost --port 8000 --reload
       - streamlit run start.py
 
- run like scrypt only (from related folder: scrypt):
       - uvicorn main:app --host localhost --port 8000 --reload

# first request take a long time due LLM downloading - don't worry