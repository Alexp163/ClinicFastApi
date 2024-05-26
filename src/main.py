from fastapi import FastAPI
from admin.panel import register_admin
from database import engine

app = FastAPI()

register_admin(app, engine)

@app.get("/")
def index():
    return "Hello"

@app.get("/endpoint")
def endpoint():
    return "Endpoint"
