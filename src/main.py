import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

model = spacy.load("ru_core_news_lg")

app = FastAPI()

class UserRequestIn(BaseModel):
    text: str

class EntityOut(BaseModel):
    start: int
    end: int
    type: str
    text: str

class EntitiesOut(BaseModel):
    entities: List[EntityOut]

@app.post("/entities", response_model=EntitiesOut)
def read_entities(user_request_in: UserRequestIn):
    doc = model(user_request_in.text)

    return {
        "entities": [
            {
                "start": ent.start_char,
                "end": ent.end_char,
                "type": ent.label_,
                "text": ent.text,
            } for ent in doc.ents
        ]
    }