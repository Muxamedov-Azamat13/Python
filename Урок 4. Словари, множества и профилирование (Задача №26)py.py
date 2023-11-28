# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

def exponentiation(a, b):
    if b == 0:
        return 1
    else:
        return a * exponentiation(a, b - 1)

res = exponentiation(a, b)
print(f'A = {a}; B = {b} -> {res}')
