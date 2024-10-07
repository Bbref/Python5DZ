# bank.py

def print_menu():
    print('\n=== Банковский счет ===')
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')


def deposit(balance):
    try:
        amount = float(input('Введите сумму для пополнения счета: '))
        if amount <= 0:
            print('Сумма должна быть положительной.')
            return balance
        balance += amount
        print(f'Счет пополнен на {amount} руб. Текущий баланс: {balance} руб.')
        return balance
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите число.')
        return balance


def make_purchase(balance, history):
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
            history.append((description, amount))
            print(f'Покупка "{description}" на сумму {amount} руб. выполнена. Текущий баланс: {balance} руб.')
        return balance, history
    except ValueError:
        print('Некорректный ввод. Пожалуйста, введите число.')
        return balance, history


def show_history(history):
    if not history:
        print('История покупок пуста.')
    else:
        print('История покупок:')
        for idx, (description, amount) in enumerate(history, start=1):
            print(f'{idx}. Название: {description}, Сумма: {amount} руб.')


def bank_account():
    balance = 0  # Начальный баланс
    history = []

    while True:
        print_menu()
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
