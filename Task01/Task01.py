# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

date = input("Введите цифру, обозначающую день недели: ")
if date == '6' or date == '7':
    print('Выходной')
else:
    print('День рабочий')
