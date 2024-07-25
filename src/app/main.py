from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "FastAPI running in a Docker container"}