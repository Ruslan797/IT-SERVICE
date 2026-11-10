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

def test_transfer_skips_different_file_by_default(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()

    (source / "example.txt").write_text("NEW")
    (destination / "example.txt").write_text("OLD")
    (source / "missing.txt").write_text("COPY ME")

    result = transfer_files(source, destination)

    assert (destination / "example.txt").read_text() == "OLD"
    assert (destination / "missing.txt").read_text() == "COPY ME"
    assert result == {
        "planned_files": 1,
        "copied_files": 1,
        "verified_files": 1,
        "failed_files": 0,
        "skipped_files": 1,
    }


def test_transfer_overwrites_when_explicitly_allowed(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()

    (source / "example.txt").write_text("NEW")
    (destination / "example.txt").write_text("OLD")

    result = transfer_files(source, destination, overwrite=True)

    assert (destination / "example.txt").read_text() == "NEW"
    assert result == {
        
        "planned_files": 1,
        "copied_files": 1,
        "verified_files": 1,
        "failed_files": 0,
        "skipped_files": 0,
    }