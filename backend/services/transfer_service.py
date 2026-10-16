from pathlib import Path

from tools.data_transfer.comparator import compare_folders
from tools.data_transfer.copier import copy_file
from tools.data_transfer.verifier import verify_file


def transfer_files(source_path, destination_path):
    source_root = Path(source_path)
    destination_root = Path(destination_path)

    missing_files, different_files = compare_folders(
        source_root,
        destination_root,
    )

    files_to_copy = missing_files + different_files

    copied_files = 0
    verified_files = 0
    failed_files = 0

    for source_file in files_to_copy:
        try:
            destination_file = copy_file(
                source_file,
                source_root,
                destination_root,
            )

            copied_files += 1

            if verify_file(source_file, destination_file):
                verified_files += 1
            else:
                failed_files += 1

        except OSError:
            failed_files += 1

    return {
        "planned_files": len(files_to_copy),
        "copied_files": copied_files,
        "verified_files": verified_files,
        "failed_files": failed_files,
    }