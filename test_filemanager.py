import pytest
from victory import quiz_game
from bank import bank_account
from main import (
    create_folder,
    delete_item,
    copy_item,
    view_contents,
    view_folders,
    view_files,
    os_info,
    program_creator
)

# Фикстура для создания временной директории
@pytest.fixture
def temp_dir(tmp_path):
    """
    Фикстура, предоставляющая временную директорию для тестов.
    Использует встроенную фикстуру `tmp_path` от pytest.
    """
    return tmp_path

# Тест для функции создания папки
def test_create_folder(temp_dir, monkeypatch, capsys):
    """
    Тестирует функцию `create_folder`, проверяя, что папка создается правильно.
    Использует `monkeypatch` для мокирования ввода пользователя и `capsys` для захвата вывода.
    """
    folder_name = "test_folder"
    # Мокируем функцию input, чтобы она возвращала folder_name
    monkeypatch.setattr('builtins.input', lambda _: folder_name)

    # Вызываем функцию, которая должна создать папку
    create_folder(temp_dir)

    # Захватываем вывод (опционально, если нужно проверить сообщения)
    captured = capsys.readouterr()
    assert f"Папка '{folder_name}' успешно создана." in captured.out, "Сообщение о создании папки отсутствует или неверно."

    # Проверяем, что папка была создана
    assert (temp_dir / folder_name).is_dir(), f"Папка '{folder_name}' не была создана."

# Тест для удаления файла/папки
def test_delete_item(temp_dir, monkeypatch, capsys):
    """
    Тестирует функцию `delete_item`, проверяя, что папка удаляется правильно.
    Создает папку, затем удаляет ее и проверяет результат.
    """
    folder_name = "test_folder"
    # Создаем папку для удаления
    (temp_dir / folder_name).mkdir()

    # Мокируем input, чтобы функция получила имя папки для удаления
    monkeypatch.setattr('builtins.input', lambda _: folder_name)

    # Вызываем функцию, которая должна удалить папку
    delete_item(temp_dir)

    # Захватываем вывод (опционально, если нужно проверить сообщения)
    captured = capsys.readouterr()
    assert f"Папка '{folder_name}' успешно удалена." in captured.out, "Сообщение об удалении папки отсутствует или неверно."

    # Проверяем, что папка была удалена
    assert not (temp_dir / folder_name).exists(), f"Папка '{folder_name}' не была удалена."

# Тест для копирования файла/папки
def test_copy_item(temp_dir, monkeypatch, capsys):
    """
    Тестирует функцию `copy_item`, проверяя, что папка копируется правильно.
    Создает исходную папку, затем копирует ее и проверяет результат.
    """
    source_folder = temp_dir / "source_folder"
    dest_folder = temp_dir / "dest_folder"

    # Создаем исходную папку для копирования
    source_folder.mkdir()

    # Мокируем input для функции copy_item: сначала источник, затем назначение
    inputs = iter(["source_folder", "dest_folder"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Вызываем функцию копирования
    copy_item(temp_dir)

    # Захватываем вывод (опционально, если нужно проверить сообщения)
    captured = capsys.readouterr()
    assert f"Папка '{source_folder.name}' успешно скопирована как '{dest_folder.name}'." in captured.out, "Сообщение о копировании папки отсутствует или неверно."

    # Проверяем, что папка была скопирована
    assert dest_folder.is_dir(), f"Папка '{dest_folder}' не была скопирована."

# Тест для просмотра содержимого рабочей директории (непустой)
def test_view_contents_nonempty(temp_dir, capsys):
    """
    Тестирует функцию `view_contents`, проверяя, что содержимое директории выводится правильно.
    Создает файл в директории и проверяет, что он отображается в выводе.
    """
    file_path = temp_dir / "file1.txt"
    file_path.touch()  # Создаем файл в временной директории

    # Вызываем функцию, которая выводит содержимое директории
    view_contents(temp_dir)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что файл появился в выводе
    assert "file1.txt" in captured.out, "Файл 'file1.txt' не найден в выводе."

# Тест для просмотра только папок
def test_view_folders(temp_dir, capsys):
    """
    Тестирует функцию `view_folders`, проверяя, что выводятся только папки.
    Создает папку и проверяет, что она отображается в выводе.
    """
    folder_name = "test_folder"
    (temp_dir / folder_name).mkdir()  # Создаем папку

    # Вызываем функцию, которая выводит только папки
    view_folders(temp_dir)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что папка появилась в выводе
    assert folder_name in captured.out, f"Папка '{folder_name}' не найдена в выводе."

# Тест для просмотра только файлов
def test_view_files(temp_dir, capsys):
    """
    Тестирует функцию `view_files`, проверяя, что выводятся только файлы.
    Создает файл и проверяет, что он отображается в выводе.
    """
    file_name = "file1.txt"
    (temp_dir / file_name).touch()  # Создаем файл

    # Вызываем функцию, которая выводит только файлы
    view_files(temp_dir)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что файл появился в выводе
    assert file_name in captured.out, f"Файл '{file_name}' не найден в выводе."

# Тест для просмотра информации об операционной системе
def test_os_info(capsys):
    """
    Тестирует функцию `os_info`, проверяя, что информация об ОС выводится правильно.
    """
    os_info()  # Вызываем функцию
    captured = capsys.readouterr()  # Захватываем вывод

    # Проверяем, что вывод содержит информацию об ОС
    assert "Система:" in captured.out, "Информация об ОС не была выведена."

# Тест для отображения информации о создателе программы
def test_program_creator(capsys):
    """
    Тестирует функцию `program_creator`, проверяя, что информация о создателе выводится правильно.
    """
    program_creator()  # Вызываем функцию
    captured = capsys.readouterr()  # Захватываем вывод

    # Проверяем, что вывод содержит имя создателя
    assert "Создатель консольного файлового менеджера" in captured.out, "Информация о создателе не была выведена."

# Тест для викторины
def test_quiz_game(monkeypatch, capsys):
    """
    Тестирует функцию `quiz_game`, проверяя, что правильные ответы засчитываются верно.
    Мокирует ввод пользователя для предоставления правильных ответов.
    """
    # Предположим, что викторина задает 5 вопросов
    # Мокируем правильные ответы пользователя
    answers = [
        "14.03.1879",  # Альберт Эйнштейн
        "04.01.1643",  # Исаак Ньютон
        "15.02.1564",  # Галилео Галилей
        "19.11.1711",  # Михаил Ломоносов
        "09.09.1828"   # Лев Толстой
    ]
    inputs = iter(answers)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Вызываем функцию викторины
    quiz_game()

    captured = capsys.readouterr()

    # Проверяем, что вывод содержит "Правильно!" для каждого ответа
    assert captured.out.count("Правильно!") == 5, "Викторина не отработала правильно для всех ответов."

# Тест для банковского счета
def test_bank_account(monkeypatch, capsys):
    """
    Тестирует функцию `bank_account`, проверяя операции пополнения счета, совершения покупки и просмотра истории.
    Мокирует ввод пользователя для выполнения операций.
    """
    # Мокируем ввод пользователя:
    # 1. Пополнение счета: 1000
    # 2. Покупка: 500, "Test Purchase"
    # 3. История покупок
    # 4. Выход
    inputs = iter(['1', '1000', '2', '500', 'Test Purchase', '3', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Вызываем функцию банковского счета
    bank_account()

    captured = capsys.readouterr()

    # Проверяем, что баланс был пополнен
    # Исправляем ожидаемое значение с 1000 руб. на 1000.0 руб.
    assert "Текущий баланс: 1000.0 руб." in captured.out, "Пополнение счета не прошло корректно."

    # Проверяем, что покупка была выполнена
    assert 'Покупка "Test Purchase" на сумму 500.0 руб. выполнена. Текущий баланс: 500.0 руб.' in captured.out, "Покупка не прошла корректно."

    # Проверяем, что история покупок отображает сделанную покупку
    assert "История покупок:" in captured.out, "История покупок не была выведена."
    assert "Название: Test Purchase, Сумма: 500.0 руб." in captured.out, "Покупка не отображается в истории."
