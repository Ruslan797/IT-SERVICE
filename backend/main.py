from fastapi import FastAPI

from backend.api.scan import router as scan_router
from backend.api.transfer import router as transfer_router


app = FastAPI(
    title="IT-Service Data Transfer API",
    description=(
        "API for scanning, analyzing, transferring, "
        "and verifying files between computers."
    ),
    version="1.0.0",
)

app.include_router(scan_router)
app.include_router(transfer_router)


@app.get("/", tags=["System"])
def home():
    return {
        "service": "IT-Service Data Transfer API",
        "status": "running",
    }


@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}