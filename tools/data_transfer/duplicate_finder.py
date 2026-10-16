from .scanner import scan_folder
from .verifier import calculate_hash


def find_duplicates(folder_path):
    files = scan_folder(folder_path)

    files_by_size = {}

    for file in files:
        file_size = file.stat().st_size

        if file_size not in files_by_size:
            files_by_size[file_size] = []

        files_by_size[file_size].append(file)

    duplicates = {}

    for file_size, same_size_files in files_by_size.items():
        if len(same_size_files) < 2:
            continue

        files_by_hash = {}

        for file in same_size_files:
            file_hash = calculate_hash(file)

            if file_hash not in files_by_hash:
                files_by_hash[file_hash] = []

            files_by_hash[file_hash].append(file)

        for file_hash, same_hash_files in files_by_hash.items():
            if len(same_hash_files) >= 2:

                duplicates[file_hash] = same_hash_files

    return duplicates


def print_duplicate_report(duplicates):
    print("\nDUPLICATE REPORT")
    print("-" * 50)

    if not duplicates:
        print("No duplicates found.")
        return