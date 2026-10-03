from pathlib import Path


def verify_file(source_file, destination_file):
    source_file = Path(source_file)
    destination_file = Path(destination_file)

    if not destination_file.exists():
        return False

    if source_file.stat().st_size != destination_file.stat().st_size:
        return False

    return True