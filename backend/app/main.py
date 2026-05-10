from fastapi import FastAPI
from app.services.extractor import extract_knowledge
from app.DSA.entity_resolver import EntityResolver

app = FastAPI()
resolver = EntityResolver

@app.get("/")
def test():
    return {"message" : "Every thing is fine"}