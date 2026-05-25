from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {
        "status": "running",
        "service": "Creator Cut AI"
    }
