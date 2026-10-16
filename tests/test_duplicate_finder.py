from tools.data_transfer.duplicate_finder import find_duplicates


def test_find_duplicates_detects_identical_files(tmp_path):
    first_file = tmp_path / "hello.txt"
    second_file = tmp_path / "hello_copy.txt"
    different_file = tmp_path / "other.txt"

    first_file.write_text("hello")
    second_file.write_text("hello")
    different_file.write_text("other")

    duplicates = find_duplicates(tmp_path)

    duplicate_groups = list(duplicates.values())

    assert len(duplicate_groups) == 1
    assert first_file in duplicate_groups[0]
    assert second_file in duplicate_groups[0]
    assert different_file not in duplicate_groups[0]