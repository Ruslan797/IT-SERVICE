from pydantic import BaseModel, Field


class TransferRequest(BaseModel):
    source_path: str = Field(
        ...,
        description="Path to the source directory",
    )
    destination_path: str = Field(
        ...,
        description="Path to the destination directory",
    )


class TransferResponse(BaseModel):
    planned_files: int
    copied_files: int
    verified_files: int
    failed_files: int