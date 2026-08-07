from fastapi import FastAPI

from app.api.imports import router as import_router

app = FastAPI(title="InvestIQ API")

app.include_router(import_router)


@app.get("/")
def root():
    return {
        "application": "InvestIQ",
        "version": "0.1.0",
        "status": "Running"
    }