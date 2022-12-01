def task_1() -> None:
    """ Задание 1 """
    print("ЗАДАНИЕ 1")
    input_data = input("Введите 2 числа через пробел: ")
    assert len(input_data.split()) == 2, "Вы ввели не 2 числа"
    a, b = input_data.split()
    a = get_number_from_string(a)
    b = get_number_from_string(b)
    print(f"Сумма чисел: {a + b}")
    print(f"Разность чисел: {a - b}")
    print(f"Произведение чисел: {a * b}")
    print(f"Возведение в степень: {a ** b}")
    assert b != 0, "Деление на 0"
    print(f"Частное чисел: {a / b}")
    print(f"Целочисленное деление: {a // b}")
    print(f"Остаток от деления: {a % b}")
    print(f"Деление по модулю: {abs(a) % abs(b)}")
    print()


def get_number_from_string(n: str) -> int | float:
    if "/" in n or "//" in n or "%" in n:
        try:
            return eval(n)
        except Exception as e:
            raise Exception(f"Вы ввели некорректное выражение: {n}") from e
    try:
        return int(n)
    except ValueError:
        return float(n)


if __name__ == "__main__":
    task_1()
