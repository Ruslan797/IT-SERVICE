from fastapi import APIRouter

from backend.schemas.scan import ScanRequest, ScanResponse
from tools.data_transfer.scanner import scan_folder


router = APIRouter(
    prefix="/api",
    tags=["Scanning"],
)


@router.post(
    "/scan",
    response_model=ScanResponse,
    summary="Scan a directory",
)
def scan_directory(request: ScanRequest):
    files = scan_folder(request.source_path)

    total_size = sum(
        file.stat().st_size
        for file in files
    )

    return ScanResponse(
        source_path=request.source_path,
        total_files=len(files),
        total_size_bytes=total_size,
    )