# test_bank.py

import pytest
import json
from pathlib import Path
from bank import load_balance, save_balance, load_history, save_history


@pytest.fixture
def temp_dir(tmp_path, monkeypatch):
    """
    Фикстура для создания временной директории и перенаправления путей к файлам.
    """
    # Создаём временную директорию
    temp_directory = tmp_path / "bank_test"
    temp_directory.mkdir()

    # Перенаправляем BALANCE_FILE и HISTORY_FILE на файлы в временной директории
    monkeypatch.setattr('bank.BALANCE_FILE', temp_directory / "balance.json")
    monkeypatch.setattr('bank.HISTORY_FILE', temp_directory / "history.json")

    return temp_directory


def test_load_balance_no_file(temp_dir):
    """
    Тестирует load_balance, когда balance.json не существует.
    Ожидается, что функция вернёт 0.
    """
    balance = load_balance()
    assert balance == 0, "Баланс должен быть 0, когда файл не существует."


def test_load_balance_valid_file(temp_dir):
    """
    Тестирует load_balance, когда balance.json существует и содержит валидные данные.
    Ожидается, что функция вернёт сохранённый баланс.
    """
    # Подготовка файла balance.json с валидными данными
    balance_data = {"balance": 1500.0}
    (temp_dir / "balance.json").write_text(json.dumps(balance_data), encoding='utf-8')

    balance = load_balance()
    assert balance == 1500.0, "Баланс должен быть 1500.0, как указано в файле."


def test_load_balance_invalid_file(temp_dir, capsys):
    """
    Тестирует load_balance, когда balance.json существует, но содержит невалидные данные.
    Ожидается, что функция вернёт 0 и выведет сообщение об ошибке.
    """
    # Подготовка файла balance.json с невалидными данными
    (temp_dir / "balance.json").write_text("invalid json", encoding='utf-8')

    balance = load_balance()
    assert balance == 0, "Баланс должен быть 0 при некорректном содержимом файла."

    # Проверка вывода сообщения об ошибке
    captured = capsys.readouterr()
    assert "Ошибка при чтении файла баланса. Устанавливаем баланс в 0." in captured.out, "Сообщение об ошибке отсутствует или неверно."


def test_save_balance(temp_dir):
    """
    Тестирует save_balance, проверяя, что баланс сохраняется корректно в balance.json.
    """
    balance_to_save = 2000.0
    save_balance(balance_to_save)

    # Проверка существования файла
    balance_file = temp_dir / "balance.json"
    assert balance_file.exists(), "Файл balance.json должен быть создан."

    # Проверка содержимого файла
    with balance_file.open('r', encoding='utf-8') as f:
        data = json.load(f)
        assert data.get('balance') == balance_to_save, "Сохранённый баланс должен соответствовать переданному значению."


def test_load_history_no_file(temp_dir):
    """
    Тестирует load_history, когда history.json не существует.
    Ожидается, что функция вернёт пустой список.
    """
    history = load_history()
    assert history == [], "История должна быть пустой, когда файл не существует."


def test_load_history_valid_file(temp_dir):
    """
    Тестирует load_history, когда history.json существует и содержит валидные данные.
    Ожидается, что функция вернёт сохранённую историю.
    """
    # Подготовка файла history.json с валидными данными
    history_data = {
        "history": [
            {"description": "Книга", "amount": 500.0},
            {"description": "Продукты", "amount": 1000.0}
        ]
    }
    (temp_dir / "history.json").write_text(json.dumps(history_data), encoding='utf-8')

    history = load_history()
    assert history == history_data['history'], "История должна соответствовать данным в файле."


def test_load_history_invalid_file(temp_dir, capsys):
    """
    Тестирует load_history, когда history.json существует, но содержит невалидные данные.
    Ожидается, что функция вернёт пустой список и выведет сообщение об ошибке.
    """
    # Подготовка файла history.json с невалидными данными
    (temp_dir / "history.json").write_text("invalid json", encoding='utf-8')

    history = load_history()
    assert history == [], "История должна быть пустой при некорректном содержимом файла."

    # Проверка вывода сообщения об ошибке
    captured = capsys.readouterr()
    assert "Ошибка при чтении файла истории покупок. Устанавливаем пустую историю." in captured.out, "Сообщение об ошибке отсутствует или неверно."


def test_save_history(temp_dir):
    """
    Тестирует save_history, проверяя, что история покупок сохраняется корректно в history.json.
    """
    history_to_save = [
        {"description": "Книга", "amount": 500.0},
        {"description": "Продукты", "amount": 1000.0}
    ]
    save_history(history_to_save)

    # Проверка существования файла
    history_file = temp_dir / "history.json"
    assert history_file.exists(), "Файл history.json должен быть создан."

    # Проверка содержимого файла
    with history_file.open('r', encoding='utf-8') as f:
        data = json.load(f)
        assert data.get(
            'history') == history_to_save, "Сохранённая история должна соответствовать переданному значению."
