import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive  # Принимает на вход текст, делает первую букву заглавной
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("hello Hello world", "Hello Hello world")  # с вводной заглавной буквой
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # числа в начале
    ("", ""),  # пустая строка
    ("   ", "   "),  # пробел
    ("235 66", "235 66"),  # числа
    ("!@#$%^", "!@#$%^")  # символы
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive  # Принимает на вход текст и удаляет пробелы в начале
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro   ", "skypro   "),
    ("   hello world", "hello world"),
    ("  python", "python"),
    ("  test string", "test string"),
    ("    leading spaces", "leading spaces")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("no spaces", "no spaces"),     # без пробелов
    ("trailing   ", "trailing   "),  # пробелы в конце
    (" mixed   ", "mixed   "),     # смешанные пробелы
    ("", ""),                      # пусто
    ("!@#$% ", "!@#$% ")           # символы с пробелами
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive  # Возвращает `True`, если строка содержит искомый
# символ и `False` - если нет
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Hello", "l", True),
    ("Python", "P", True),
    ("Test123", "3", True),
    ("Special!@#", "#", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("Hello", "z", False),
    ("", "a", False),            # пустая строка
    ("12345", "6", False),
    ("Special", "!", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello", "l", "Heo"),
    ("Python", "P", "ython"),
    ("12345", "3", "1245"),
    ("Special!@#", "!", "Special@#")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", "SkyPro"),       # символа нет в строке
    ("Hello", "z", "Hello"),        # символа нет в строке
    ("", "a", ""),                  # пустая строка
    ("12345", "6", "12345"),       # символа нет в строке
    ("Special", "!", "Special"),    # символа нет в строке
    ("test", "T", "test"),         # регистрозависимая проверка
    ("abc", "ABC", "abc"),         # проверка на подстроку
    ("abc", "", "abc"),            # пустой символ для удаления
    ("abc", " ", "abc")           # пробел как символ для удаления
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
