from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello"

@app.get("/endpoint")
def endpoint():
    return "Endpoint"
