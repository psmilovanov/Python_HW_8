# Задание 1.

class Date():
    date_string: str

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def transform(cls, date_string):
        a = date_string.split('-')
        return [int(a[0]), int(a[1]), int(a[2])]

    @staticmethod
    def valid(int_string):
        if (int_string[1] > 12 or int_string[1] < 1):
            return f"Неправильный формат. Номер месяца не может быть больше 12 и меньше 1."
        elif int_string[0] < 1:
            return f"Неправильный формат. Номер дня не может быть меньше 1."
        elif int_string[1] in [1, 3, 5, 7, 8, 10, 12]:
            if (int_string[0] > 31):
                return f"Неправильный формат. В месяце с номером {int_string[1]} должно быть меньше 31 дня"
            else:
                return f"Все ок"
        elif int_string[1] in [4, 6, 9, 11]:
            if (int_string[0] > 30):
                return f"Неправильный формат. В месяце {int_string[1]} должно быть меньше 30 дней"
            else:
                return f"Все ок"
        else:
            if int_string[2] % 4 == 0:
                if int_string[0] > 29:
                    return f"Неправильный формат. В феврале високосного года должно быть  меньше 29 дней"
                else:
                    return f"Все ок"
            else:
                if int_string[0] > 28:
                    return f"Неправильный формат. В феврале невисокосного года должно быть меньше 28 дней"
                else:
                    return f"Все ок"


example_string = "29-02-2021"

print(Date.valid(Date.transform(example_string)))
