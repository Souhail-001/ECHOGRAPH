from fastapi import FastAPI
from neo4j import GraphDatabase
import os

app = FastAPI()

@app.get("/")
def test():
    return {"message" : "Every thing is fine"}