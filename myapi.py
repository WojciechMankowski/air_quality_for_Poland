from fastapi import FastAPI, __version__
from read import CreatAPI
from ContextManager import ContextManager
app = FastAPI()

@app.get('/')
def index():
    print(__version__)
    return {"Witaj": "Na mojej strinie!! :)"}

@app.get('/{city}')
def home(city: str):
    ContextManager(city=city)
    api = CreatAPI()
    return api

