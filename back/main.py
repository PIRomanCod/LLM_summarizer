import time
import uvicorn

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from src.database.db import get_db
from src.routes import chat

app = FastAPI()

origins = ["*",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def custom_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    during = time.time() - start_time
    response.headers['performance'] = str(during)
    return response


@app.middleware("http")
async def errors_handling(request: Request, call_next):
    """
    The errors_handling function is a middleware that catches any exception raised by the application.
    It returns an error response with status code 500 and a JSON body containing the reason for the error.

    :param request: Request: Access the request object
    :param call_next: Pass the request to the next handler in the pipeline
    :return: A json response object with a 500 status code and the reason for the error
    """
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(status_code=500, content={'reason': str(exc)})


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    """
    The healthchecker function is a simple function that checks the health of the database.
    It does this by making a request to the database and checking if it returns any results.
    If there are no results, then we know something is wrong with our connection.

    :param db: Session: Pass in the database session
    :return: A dictionary with a message
    """
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


app.include_router(chat.router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
