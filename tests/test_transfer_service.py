from backend.services.transfer_service import transfer_files


def test_transfer_files_copies_and_verifies_file(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "destination"

    source.mkdir()
    destination.mkdir()

    source_file = source / "hello.txt"
    source_file.write_text("hello")

    result = transfer_files(source, destination)

    destination_file = destination / "hello.txt"

    assert destination_file.exists()
    assert destination_file.read_text() == "hello"

    assert result["planned_files"] == 1
    assert result["copied_files"] == 1
    assert result["verified_files"] == 1
    assert result["failed_files"] == 0