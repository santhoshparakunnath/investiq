from fastapi import FastAPI

app = FastAPI(title="InvestIQ API")

@app.get("/")
def root():
    return {
        "application": "InvestIQ",
        "version": "0.1.0",
        "status": "Running"
    }