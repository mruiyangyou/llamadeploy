from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List 
from app.model import model_query

# define prompt class
class Query(BaseModel):
    prompt: str
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

@app.get("/query")
async def root(query: Query):
    res = model_query(query=query.prompt)
    return {"message": f"{res}"}