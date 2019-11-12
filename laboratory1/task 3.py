import re


def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}(\.[0-9]{1,})?$', value)):
            flag = False
            value = float(value)
        else:
            print('Помилка')
    return value

x = do_input_float("Введіть число \n")
if x > 3:
    x = 1.2 * x ** 2 - 3 * x - 9
    print("Значкння x =", x)
else:
    x = 12.1 / (2 * x ** 2 + 1)
    print("Значення x =", x)