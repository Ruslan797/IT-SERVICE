from .scanner import scan_folder


def analyze_folder(folder_path):
    files = scan_folder(folder_path)

    file_count = 0
    total_size = 0

    for file in files:
        file_count += 1
        total_size += file.stat().st_size

    return file_count, total_size


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"

    size_kb = size_bytes / 1024

    if size_kb < 1024:
        return f"{size_kb:.2f} KB"

    size_mb = size_kb / 1024

    if size_mb < 1024:
        return f"{size_mb:.2f} MB"

    size_gb = size_mb / 1024

    return f"{size_gb:.2f} GB"


def categorize_files(folder_path):
    files = scan_folder(folder_path)

    categories = {
        "images": {"count": 0, "size": 0},
        "videos": {"count": 0, "size": 0},
        "documents": {"count": 0, "size": 0},
        "other": {"count": 0, "size": 0}
    }

    for file in files:
        extension = file.suffix.lower()
        file_size = file.stat().st_size

        if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            category = "images"

        elif extension in [".mp4", ".mov", ".avi", ".mkv"]:
            category = "videos"

        elif extension in [".pdf", ".doc", ".docx", ".txt", ".xlsx"]:
            category = "documents"

        else:
            category = "other"

        categories[category]["count"] += 1
        categories[category]["size"] += file_size

    return categories