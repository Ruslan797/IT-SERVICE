from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "IT Service is running"}