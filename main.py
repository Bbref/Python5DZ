import os
import shutil
import platform

# Импортируем функции из модулей victory и bank
from victory import quiz_game
from bank import bank_account

# Функция для создания папки
def create_folder(work_dir):
    folder_name = input("Введите название папки: ")
    path = os.path.join(work_dir, folder_name)
    try:
        os.mkdir(path)
        print(f"Папка '{folder_name}' успешно создана.\n")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует.\n")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}\n")

# Функция для удаления файла/папки
def delete_item(work_dir):
    item_name = input("Введите название файла или папки для удаления: ")
    path = os.path.join(work_dir, item_name)
    if not os.path.exists(path):
        print(f"'{item_name}' не существует в рабочей директории.\n")
        return
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл '{item_name}' успешно удален.\n")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Папка '{item_name}' успешно удалена.\n")
    except Exception as e:
        print(f"Ошибка при удалении: {e}\n")

# Функция для копирования файла/папки
def copy_item(work_dir):
    source = input("Введите название файла или папки для копирования: ")
    destination = input("Введите новое название файла или папки: ")
    src_path = os.path.join(work_dir, source)
    dest_path = os.path.join(work_dir, destination)
    if not os.path.exists(src_path):
        print(f"'{source}' не существует в рабочей директории.\n")
        return
    try:
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Файл '{source}' успешно скопирован как '{destination}'.\n")
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
            print(f"Папка '{source}' успешно скопирована как '{destination}'.\n")
    except FileExistsError:
        print(f"'{destination}' уже существует.\n")
    except Exception as e:
        print(f"Ошибка при копировании: {e}\n")

# Функция для просмотра содержимого рабочей директории
def view_contents(work_dir):
    items = os.listdir(work_dir)
    if not items:
        print("Рабочая директория пуста.\n")
    else:
        print("Содержимое рабочей директории:")
        for item in items:
            print(f"- {item}")
        print()

# Функция для просмотра только папок
def view_folders(work_dir):
    items = os.listdir(work_dir)
    folders = [item for item in items if os.path.isdir(os.path.join(work_dir, item))]
    if not folders:
        print("В рабочей директории нет папок.\n")
    else:
        print("Папки в рабочей директории:")
        for folder in folders:
            print(f"- {folder}")
        print()

# Функция для просмотра только файлов
def view_files(work_dir):
    items = os.listdir(work_dir)
    files = [item for item in items if os.path.isfile(os.path.join(work_dir, item))]
    if not files:
        print("В рабочей директории нет файлов.\n")
    else:
        print("Файлы в рабочей директории:")
        for file in files:
            print(f"- {file}")
        print()

# Функция для просмотра информации об операционной системе
def os_info():
    print("Информация об операционной системе:")
    print(f"Система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Архитектура: {platform.machine()}\n")

# Функция для отображения информации о создателе программы
def program_creator():
    print("Создатель консольного файлового менеджера - Кульков Сергей.\n")

# Функция для смены рабочей директории
def change_working_directory():
    new_dir = input("Введите путь к новой рабочей директории: ")
    if os.path.isdir(new_dir):
        try:
            os.chdir(new_dir)
            print(f"Рабочая директория изменена на: {new_dir}\n")
            return new_dir
        except Exception as e:
            print(f"Ошибка при смене директории: {e}\n")
    else:
        print("Указанная директория не существует.\n")
    return None

# Основная функция меню
def main():
    work_dir = os.getcwd()
    while True:
        print("\n=== Консольный файловый менеджер ===")
        print(f"Текущая рабочая директория: {work_dir}")
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Информация о создателе программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")
        choice = input("Выберите пункт меню (1-12): ")

        if choice == '1':
            create_folder(work_dir)
        elif choice == '2':
            delete_item(work_dir)
        elif choice == '3':
            copy_item(work_dir)
        elif choice == '4':
            view_contents(work_dir)
        elif choice == '5':
            view_folders(work_dir)
        elif choice == '6':
            view_files(work_dir)
        elif choice == '7':
            os_info()
        elif choice == '8':
            program_creator()
        elif choice == '9':
            quiz_game()  # Вызов функции викторины из victory.py
        elif choice == '10':
            bank_account()  # Вызов функции банковского счета из bank.py
        elif choice == '11':
            new_dir = change_working_directory()
            if new_dir:
                work_dir = new_dir
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 12.\n")

if __name__ == "__main__":
    main()
