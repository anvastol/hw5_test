from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

translate=pipeline("translation_ru_to_fr", model = "Helsinki-NLP/opus-mt-ru-fr")

@app.post("/predict/")
async def predict(item:Item):
    return translate(item.text)[0]
