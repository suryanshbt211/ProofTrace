from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api.validate import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
