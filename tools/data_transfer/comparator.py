from pathlib import Path
from .scanner import scan_folder
from .verifier import calculate_hash


def compare_folders(source_root, destination_root):
    source_root = Path(source_root)
    destination_root = Path(destination_root)

    source_files = scan_folder(source_root)
    destination_files = scan_folder(destination_root)

    destination_map = {}

    for file in destination_files:
        relative_path = file.relative_to(destination_root)
        destination_map[relative_path] = file

    missing_files = []
    different_files = []

    for source_file in source_files:
        relative_path = source_file.relative_to(source_root)

        if relative_path not in destination_map:
            missing_files.append(source_file)
        else:
            destination_file = destination_map[relative_path]

            if source_file.stat().st_size != destination_file.stat().st_size:
                different_files.append(source_file)
            elif calculate_hash(source_file) != calculate_hash(destination_file):
                different_files.append(source_file)

    return missing_files, different_files