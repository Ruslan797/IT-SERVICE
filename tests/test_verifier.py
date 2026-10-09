from tools.data_transfer.verifier import verify_file


def test_verify_file_detects_different_content(tmp_path):
    source_file = tmp_path / "source.txt"
    destination_file = tmp_path / "destination.txt"

    source_file.write_text("AAAAA")
    destination_file.write_text("BBBBB")

    result = verify_file(source_file, destination_file)

    assert result is False