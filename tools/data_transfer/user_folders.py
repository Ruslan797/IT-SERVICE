from pathlib import Path
import shutil
from tools.data_transfer.analyzer import format_size
from .scanner import scan_folder


def find_user_folders():
    home = Path.home()

    folder_names = [
        "Desktop",
        "Documents",
        "Downloads",
        "Pictures",
        "Videos",
    ]

    folders = []

    for name in folder_names:
        folder = home / name

        if folder.exists() and folder.is_dir():
            folders.append(folder)

    return folders


def get_folder_size(folder):
    total_size = 0

    for item in folder.rglob("*"):
        if item.is_file():
            total_size += item.stat().st_size

    return total_size

def analyze_user_folders():
    folders = find_user_folders()
    result = []

    for folder in folders:
        size = get_folder_size(folder)

        result.append({
            "name": folder.name,
            "path": folder,
            "size": size,
        })

    return result


def print_user_folders():
    folders = analyze_user_folders()

    print("\nUSER DATA")
    print("-" * 50)

    for folder in folders:
        print(
            f"{folder['name']:<12} "
            f"{format_size(folder['size']):>10}  "
            f"{folder['path']}"
        )


def select_user_folders(folders):
    print("\nSELECT FOLDERS TO TRANSFER")
    print("-" * 50)

    for number, folder in enumerate(folders, start=1):
        print(
            f"{number}. "
            f"{folder['name']:<12} "
            f"{format_size(folder['size']):>10}"
        )

    choice = input(
        "\nEnter folder numbers separated by commas "
        "(example: 1,3,4): "
    )

    selected = []

    for value in choice.split(","):
        value = value.strip()

        if value.isdigit():
            index = int(value) - 1

            if 0 <= index < len(folders):
                selected.append(folders[index])

    return selected


def calculate_selected_size(selected_folders):
    total_size = 0

    for folder in selected_folders:
        total_size += folder["size"]

    return total_size


def check_destination_space(destination, required_size):
    destination = Path(destination)

    if not destination.exists():
        print("Error: destination does not exist.")
        return False

    if not destination.is_dir():
        print("Error: destination is not a folder.")
        return False

    disk_usage = shutil.disk_usage(destination)
    free_space = disk_usage.free

    print(f"Required space: {format_size(required_size)}")
    print(f"Free space:     {format_size(free_space)}")

    return free_space >= required_size


if __name__ == "__main__":
    folders = analyze_user_folders()
    selected = select_user_folders(folders)
    total_size = calculate_selected_size(selected)

    print("\nSELECTED FOR TRANSFER")
    print("-" * 50)

    for folder in selected:
        print(
            f"{folder['name']:<12} "
            f"{format_size(folder['size']):>10}  "
            f"{folder['path']}"
        )

    print("-" * 50)
    print(f"Total: {format_size(total_size)}")
    
    destination = input("\nDestination folder: ").strip()

    if check_destination_space(destination, total_size):
        print("Enough free space.")
    else:
        print("Not enough free space or invalid destination.")