"""FastAPI is a modern and high-performance Python web framework used to build APIs quickly and efficiently. Designed with simplicity it allows developers to create RESTful APIs using Python's type hints which also enable automatic validation and error handling.

One of FastAPI’s key features is its ability to generate interactive API documentation automatically making it easier to test
and understand API endpoints.
It is an ideal choice for beginners and professionals who want to build fast, secure and scalable web applications with minimal effort.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/getgreetings")
def getuser():
    return "Hello, Welcome to FastAPI."

@app.get("/getgreetings/{greeting_id}")
def getuserbyid(greeting_id: int):
    return {"userid": greeting_id}