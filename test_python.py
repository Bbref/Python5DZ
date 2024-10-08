# test_python.py

import math
import pytest

# Тесты для функции filter
def test_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    assert even == [2, 4, 6], "Фильтрация четных чисел не работает правильно"

def test_filter_non_empty_strings():
    strings = ["apple", "", "banana", "", "cherry"]
    non_empty = list(filter(None, strings))
    assert non_empty == ["apple", "banana", "cherry"], "Фильтрация пустых строк не работает правильно"

# Тесты для функции map
def test_map_square_numbers():
    numbers = [1, 2, 3, 4]
    squares = list(map(lambda x: x**2, numbers))
    assert squares == [1, 4, 9, 16], "Квадрат чисел вычисляется неверно"

def test_map_uppercase_strings():
    strings = ["apple", "banana", "cherry"]
    uppercased = list(map(str.upper, strings))
    assert uppercased == ["APPLE", "BANANA", "CHERRY"], "Преобразование строк в верхний регистр не работает правильно"

# Тесты для функции sorted
def test_sorted_numbers():
    numbers = [5, 2, 9, 1]
    sorted_numbers = sorted(numbers)
    assert sorted_numbers == [1, 2, 5, 9], "Сортировка чисел работает неверно"

def test_sorted_strings_reverse():
    strings = ["banana", "apple", "cherry"]
    sorted_strings = sorted(strings, reverse=True)
    assert sorted_strings == ["cherry", "banana", "apple"], "Обратная сортировка строк не работает правильно"

# Тесты для функций из библиотеки math
def test_math_pi():
    assert math.pi == 3.141592653589793, "Значение math.pi неверно"

def test_math_sqrt():
    assert math.sqrt(16) == 4, "Квадратный корень из 16 должен быть 4"
    assert math.sqrt(2) == pytest.approx(1.41421356), "Квадратный корень из 2 вычислен неверно"

def test_math_pow():
    assert math.pow(2, 3) == 8.0, "2 в степени 3 должно быть 8.0"
    assert math.pow(5, 0) == 1.0, "5 в степени 0 должно быть 1.0"

def test_math_hypot():
    assert math.hypot(3, 4) == 5.0, "Гипотенуза для (3, 4) должна быть 5.0"
    assert math.hypot(5, 12) == 13.0, "Гипотенуза для (5, 12) должна быть 13.0"

# Дополнительные тесты для углубленного покрытия
def test_filter_no_matches():
    numbers = [1, 3, 5]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    assert even == [], "Фильтрация без совпадений должна возвращать пустой список"

def test_map_empty_input():
    numbers = []
    result = list(map(lambda x: x * 2, numbers))
    assert result == [], "Функция map с пустым вводом должна возвращать пустой список"

def test_sorted_with_duplicates():
    numbers = [4, 2, 2, 3, 4]
    sorted_numbers = sorted(numbers)
    assert sorted_numbers == [2, 2, 3, 4, 4], "Сортировка с дубликатами работает неверно"
