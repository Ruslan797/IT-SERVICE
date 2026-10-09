from tools.data_transfer.scanner import scan_folder


def test_scan_folder_finds_files(tmp_path):
    test_file = tmp_path / "hello.txt"
    test_file.write_text("hello")

    files = scan_folder(tmp_path)

    assert test_file in files