# Задание 2.
class Zexception(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(div_1, div_2):
    if div_2 == 0:
        raise Zexception("Деление на 0 невозможно")
    else:
        return (div_1 / div_2)


div_1 = float(input("Введите делимое: "))
div_2 = float(input("Введите делитель: "))

try:
    print(division(div_1, div_2))
except Zexception as z_except:
    print(z_except)
