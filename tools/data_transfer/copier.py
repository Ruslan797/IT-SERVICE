import shutil
from pathlib import Path


def copy_file(source_file, source_root, destination_root):
    source_file = Path(source_file)
    source_root = Path(source_root)
    destination_root = Path(destination_root)

    relative_path = source_file.relative_to(source_root)
    destination_file = destination_root / relative_path

    destination_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(source_file, destination_file)

    return destination_file