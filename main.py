
def get_multiplied_digits(number):
    """Функция рекурсивным вызовом подсчитывает произведение цифр переданного ей числа"""
    str_number = str(number)        # Переменная хранит строковое представление аргумента
    first = int(str_number[0])      # Получим первую цифру числа
    if len(str_number) > 1:         # Если длина строки больше 1
        return first * get_multiplied_digits(int(str_number[1:]))   # Рекурсивный вызов функции
    else:
        return first                # Возвращает оставшуюся цифру

result = get_multiplied_digits(40203)
print(result)
