from pathlib import Path
import shutil

from .comparator import compare_folders
from .analyzer import analyze_folder, format_size, categorize_files
from .copier import copy_file
from .verifier import verify_file


source_root = input("Enter source folder: ")
destination_root = input("Enter destination folder: ")

source_root = Path(source_root)
destination_root = Path(destination_root)

if not source_root.exists():
    print("Error: source folder does not exist.")
    raise SystemExit

if not source_root.is_dir():
    print("Error: source path is not a folder.")
    raise SystemExit

if not destination_root.exists():
    print("Error: destination folder does not exist.")
    raise SystemExit

if not destination_root.is_dir():
    print("Error: destination path is not a folder.")
    raise SystemExit

file_count, total_size = analyze_folder(source_root)

print("SOURCE ANALYSIS")
print("Files:", file_count)
print("Size:", format_size(total_size))

missing_files, different_files = compare_folders(
    source_root,
    destination_root
)

print("MISSING FILES:", missing_files)
print("DIFFERENT FILES:", different_files)

categories = categorize_files(source_root)

print("\nFILE CATEGORIES")

print(
    "Images:",
    categories["images"]["count"],
    "files |",
    format_size(categories["images"]["size"])
)

print(
    "Videos:",
    categories["videos"]["count"],
    "files |",
    format_size(categories["videos"]["size"])
)

print(
    "Documents:",
    categories["documents"]["count"],
    "files |",
    format_size(categories["documents"]["size"])
)

print(
    "Other:",
    categories["other"]["count"],
    "files |",
    format_size(categories["other"]["size"])
)

files_to_copy = missing_files + different_files

if different_files:
    print("\nWARNING")
    print("-" * 50)
    print(
        len(different_files),
        "file(s) already exist in the destination but are different."
    )
    print("These files will be overwritten.")

    answer = input("Continue? (yes/no): ").strip().lower()

    if answer != "yes":
        print("Transfer cancelled.")
        raise SystemExit

copy_size = 0

for file in files_to_copy:
    copy_size += file.stat().st_size

disk_usage = shutil.disk_usage(destination_root)
free_space = disk_usage.free

print("\nTRANSFER PLAN")
print("Files to copy:", len(files_to_copy))
print("Size to copy:", format_size(copy_size))
print("Free space:", format_size(free_space))

if copy_size > free_space:
    print("Error: not enough free space.")
    raise SystemExit

if len(files_to_copy) == 0:
    print("\nNothing to copy.")
    raise SystemExit

answer = input("\nStart copying? (yes/no): ").strip().lower()

if answer == "yes":
    copied_count = 0
    verified_count = 0
    failed_count = 0
    errors = []

    for file in files_to_copy:
        try:
            destination_file = copy_file(
                file,
                source_root,
                destination_root
            )

            copied_count += 1

            if verify_file(file, destination_file):
                verified_count += 1
                print("Verified:", destination_file)
            else:
                failed_count += 1
                errors.append(
                    f"{file} -> verification failed"
                )
                print("Verification failed:", destination_file)

        except OSError as error:
            failed_count += 1
            errors.append(
                f"{file} -> {error}"
            )
            print("Copy failed:", file)
            print("Reason:", error)

    print("\nTRANSFER REPORT")
    print("-" * 50)
    print("Missing files:", len(missing_files))
    print("Different files:", len(different_files))
    print("Planned:", len(files_to_copy))
    print("Copied:", copied_count)
    print("Verified:", verified_count)
    print("Failed:", failed_count)
    print("Transferred:", format_size(copy_size))
    if errors:
        print("\nERRORS")
        print("-" * 50)

        for error in errors:
            print(error)

else:
    print("\nTransfer cancelled.")