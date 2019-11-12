import re


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



N=do_input_int("Введіть межі піднесення до квадрату\n")
for i in range(N):
     if N > 0:
        if i * i <= N:
             k = i
        else:
            print("Введіть додатне число")
print("Найбільше ціле число K =",k)