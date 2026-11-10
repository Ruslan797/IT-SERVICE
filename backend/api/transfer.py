from fastapi import APIRouter

from backend.schemas.transfer import TransferRequest, TransferResponse
from backend.services.transfer_service import transfer_files


router = APIRouter(
    prefix="/api",
    tags=["Transfer"],
)


@router.post(
    "/transfer",
    response_model=TransferResponse,
    summary="Transfer files",
)
def transfer_data(request: TransferRequest):
    return transfer_files(
        source_path=request.source_path,
        destination_path=request.destination_path,
        overwrite=request.overwrite,
    )