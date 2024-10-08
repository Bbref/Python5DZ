# bank.py

import os
import json
from pathlib import Path


def print_menu(balance):
    """
    Выводит меню банковского счета, включая текущий баланс.

    :param balance: Текущий баланс счета.
    """
    print('\n=== Банковский счет ===')
    print(f'Текущий баланс: {balance} руб.')
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')


# Определяем пути к файлам для хранения баланса и истории покупок
BALANCE_FILE = Path(__file__).parent / "balance.json"
HISTORY_FILE = Path(__file__).parent / "history.json"


def load_balance():
    """
    Загружает баланс из файла. Если файл не существует, возвращает 0.
    """
    if BALANCE_FILE.exists():
        try:
            with BALANCE_FILE.open('r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("balance", 0)
        except (json.JSONDecodeError, IOError):
            print("Ошибка при чтении файла баланса. Устанавливаем баланс в 0.")
            return 0
    else:
        return 0


def save_balance(balance):
    """
    Сохраняет баланс в файл.

    :param balance: Текущий баланс счета.
    """
    try:
        with BALANCE_FILE.open('w', encoding='utf-8') as f:
            json.dump({"balance": balance}, f, ensure_ascii=False, indent=4)
    except IOError:
        print("Ошибка при сохранении баланса.")


def load_history():
    """
    Загружает историю покупок из файла. Если файл не существует, возвращает пустой список.
    """
    if HISTORY_FILE.exists():
        try:
            with HISTORY_FILE.open('r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("history", [])
        except (json.JSONDecodeError, IOError):
            print("Ошибка при чтении файла истории покупок. Устанавливаем пустую историю.")
            return []
    else:
        return []


def save_history(history):
    """
    Сохраняет историю покупок в файл.

    :param history: Список покупок.
    """
    try:
        with HISTORY_FILE.open('w', encoding='utf-8') as f:
            json.dump({"history": history}, f, ensure_ascii=False, indent=4)
    except IOError:
        print("Ошибка при сохранении истории покупок.")


def deposit(balance):
    """
    Позволяет пополнить счет на указанную сумму.

    :param balance: Текущий баланс счета.
    :return: Обновленный баланс.
    """
    try:
        amount = float(input('Введите сумму для пополнения счета: '))
        if amount <= 0:
            print('Сумма должна быть положительной.')
            return balance
        balance += amount
        print(f'Счет пополнен на {amount} руб. Текущий баланс: {balance} руб.')
        save_balance(balance)  # Сохраняем баланс после пополнения
        return balance
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите число.')
        return balance


def make_purchase(balance, history):
    """
    Позволяет совершить покупку, уменьшая баланс и добавляя запись в историю покупок.

    :param balance: Текущий баланс счета.
    :param history: История покупок.
    :return: Обновлённый баланс и история покупок.
    """
    try:
        amount = float(input('Введите сумму покупки: '))
        if amount <= 0:
            print('Сумма покупки должна быть положительной.')
            return balance, history
        if amount > balance:
            print('Недостаточно средств на счете.')
        else:
            description = input('Введите название покупки: ')
            balance -= amount
            history.append({"description": description, "amount": amount})
            print(f'Покупка "{description}" на сумму {amount} руб. выполнена. Текущий баланс: {balance} руб.')
            save_balance(balance)  # Сохраняем баланс после покупки
            save_history(history)  # Сохраняем историю после покупки
        return balance, history
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите число.')
        return balance, history


def show_history(history):
    """
    Показывает историю покупок.

    :param history: История покупок.
    """
    if not history:
        print('История покупок пуста.')
    else:
        print('История покупок:')
        for idx, purchase in enumerate(history, start=1):
            print(f"{idx}. Название: {purchase['description']}, Сумма: {purchase['amount']} руб.")


def bank_account():
    """
    Основная функция банковского счета, обрабатывающая пользовательский ввод.
    """
    balance = load_balance()  # Загружаем баланс при запуске
    history = load_history()  # Загружаем историю покупок при запуске

    while True:
        print_menu(balance)
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            # Пополнение счета
            balance = deposit(balance)

        elif choice == '2':
            # Покупка
            balance, history = make_purchase(balance, history)

        elif choice == '3':
            # История покупок
            show_history(history)

        elif choice == '4':
            # Выход из программы
            print('Выход из банковской системы.')
            break

        else:
            print('Неверный пункт меню. Попробуйте снова.')
