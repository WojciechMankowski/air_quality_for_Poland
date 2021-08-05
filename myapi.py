from fastapi import FastAPI
from read import CreatAPI
from ContextManager import ContextManager
app = FastAPI()


@app.get('/{city}')
def home(city: str):
    ContextManager(city=city)
    api = CreatAPI()
    return api