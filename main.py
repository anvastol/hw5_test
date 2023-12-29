from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
@app.post("/predict/")
async def predict(item:Item):
    return pipe(item.text)[0]
