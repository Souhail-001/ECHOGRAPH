from pydantic import BaseModel
from typing import List

class Triple(BaseModel):
    subject : str
    relation : str
    target : str

class ExtractResult(BaseModel):
    entities : List[str]
    triples : List[Triple]