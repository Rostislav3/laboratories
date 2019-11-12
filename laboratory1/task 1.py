import re
print( """КМ-94 Малінін Ростислав Петрович
Варіант 17 Завдання 1""")
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
value1 =do_input_float("Введіть число\n")
value2 =do_input_float("Введіть число\n")
print(value1 & value2)
print(value1 | value2)
print(value1 ^ value2)