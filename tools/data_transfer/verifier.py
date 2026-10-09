from pathlib import Path
import hashlib


def calculate_hash(file_path):
    file_path = Path(file_path)
    file_hash = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(1024 * 1024):
            file_hash.update(chunk)

    return file_hash.hexdigest()


def verify_file(source_file, destination_file):
    source_file = Path(source_file)
    destination_file = Path(destination_file)

    if not destination_file.exists():
        return False

    if source_file.stat().st_size != destination_file.stat().st_size:
        return False

    source_hash = calculate_hash(source_file)
    destination_hash = calculate_hash(destination_file)

    if source_hash != destination_hash:
        return False

    return True