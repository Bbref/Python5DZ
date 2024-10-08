# test_main.py
from main import save_directory_contents


def test_save_directory_contents(tmp_path):
    """
    Тестирует функцию save_directory_contents, проверяя, что
    файл 'listdir.txt' создаётся и содержит правильные списки файлов и папок.
    """
    # Создаём несколько файлов и папок во временной директории
    files = ['file1.txt', 'file2.py', 'script.sh']
    dirs = ['dir1', 'dir2', 'dir3']

    for file in files:
        (tmp_path / file).touch()

    for dir in dirs:
        (tmp_path / dir).mkdir()

    # Вызываем функцию для сохранения содержимого директории
    save_directory_contents(tmp_path)

    # Проверяем, что файл 'listdir.txt' создан
    listdir_file = tmp_path / 'listdir.txt'
    assert listdir_file.exists(), "Файл 'listdir.txt' не был создан."

    # Читаем содержимое файла
    with listdir_file.open('r', encoding='utf-8') as f:
        content = f.read()

    # Формируем ожидаемые строки
    expected_files_line = "files: " + ", ".join(sorted(files)) + "\n"
    expected_dirs_line = "dirs: " + ", ".join(sorted(dirs)) + "\n"

    # Проверяем содержимое файла
    assert content == expected_files_line + expected_dirs_line, "Содержимое 'listdir.txt' некорректно."
