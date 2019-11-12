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


def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('Помилка')
    return value


n=do_input_int("Введіть кількість повторів\n")
x=do_input_float("Введіть значення x\n")
sum=0
for i in range(n):
    sum=sum+x/2**i
print("Значення суми",sum)