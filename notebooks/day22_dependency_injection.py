# Dependency Injection in FastAPI
from fastapi import FastAPI, Depends
app = FastAPI(title="Dependency Injection")
@app.get("/")
async def Common_Function():
    return {"Hello": "World"}

def get_name(name:str):
    return name

@app.get("/name/{name}")
async def get_name(name:str = Depends(get_name)):
    return name