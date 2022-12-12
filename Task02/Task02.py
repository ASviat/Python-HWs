#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#(расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(x):
        list.append(input(f'Введите значение {xyz[i]}: '))
    return list


def check(x):
    first = not (x[0] or x[1] or x[2])
    second = not x[0] and not x[1] and not x[2]
    result = first == second
    return result


statement = inputNumbers(3)

if check(statement) == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')