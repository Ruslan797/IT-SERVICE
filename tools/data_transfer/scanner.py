from pathlib import Path


def scan_folder(folder_path):
    folder = Path(folder_path)
    files = []

    for item in folder.rglob("*"):
        if item.is_file():
            files.append(item)

    return files