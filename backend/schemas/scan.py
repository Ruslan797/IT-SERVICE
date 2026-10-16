from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    source_path: str = Field(
        ...,
        description="Path to the directory that should be scanned",
        examples=[r"D:\Transfer_Test_Source"],
    )


class ScanResponse(BaseModel):
    source_path: str
    total_files: int
    total_size_bytes: int