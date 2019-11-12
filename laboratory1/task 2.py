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


t1 = do_input_float("Введіть кількість балів Іванова у першому турі\n")
p1 = do_input_float("Введіть кількість балів Іванова у другому турі\n")
n1 = do_input_float("Введіть кількість балів Іванова у третьому турі\n")
print("\n")

t2 =do_input_float("Введіть кількість балів Петров у першому турі\n")
p2 =do_input_float("Введіть кількість балів Петров у другому турі\n")
n2 =do_input_float("Введіть кількість балів Петров у третьому турі\n")
print("\n")

t3 =do_input_float("Введіть кількість балів Сидоров у першому турі\n")
p3 =do_input_float("Введіть кількість балів Сидоров у другому турі\n")
n3 =do_input_float("Введіть кількість балів Сидоров у третьому турі\n")
print("\n")

value1 = t1+p1+n1
value2 = t2+p2+n2
value3 = t3+p3+n3

if value1 > value2:
    if value1 > value3:
        print("Іванов виграв!!!")
    else:
          print("Сидоров виграв!!!")
elif value1 < value2:
        if value2 > value3:
            print("Петров виграв!!!")
        else:
            print("Сидоров виграв!!!")