# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# lst = "a a a b c a a d c d d".split()
# print(lst)
# dct = {}
# for item in lst:
#     if item in dct:
#         print(f"{item}_{dct[item]}", end=' ')
#     else:
#         print(item, end=' ')
#     dct[item] = dct.get(item, 0) + 1
#
# print(dct)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# twister = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells""".lower().split()
#
# print(len(set(twister)))

# Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Ваня:
#
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
#
# Петя:
#
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

# n = int(input())
# max_number = n
#
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
#
# print(max_number)

"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

# def fibonacci(n):
#     if n < 3:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
#
# n = 7
# print(fibonacci(n))
#
# fib1, fib2 = 0, 1
# for i in range(0, n):
#     fib1, fib2 = fib2, fib2 + fib1
# print(fib2)

"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

# def min_to_max(grade_list, count, x):
#     if count < 0:
#         return grade_list
#     count -= 1
#     if grade_list[count] == x:
#         grade_list[count] = min(grade_list)
#     return min_to_max(grade_list, count, x)
#
#
# list_1 = [1, 3, 3, 3, 4]
# cnt = 5
#
# print(min_to_max(list_1, cnt, max(list_1)))

"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

# def func_1(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     return flag
#
# print(func_1(10))
#
#
# def func_2(num, flag=True, i=2):
#     if i < int(num ** 0.5) + 1:
#         if num % i == 0:
#             flag = False
#         return func_2(num, flag, i+1)
#     return flag
# print(func_2(31))

"""
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

def rev(n):
    if n > 0:
        num = int(input("Введите число: "))
        rev(n - 1)
        print(num, end=' ')


rev(3)














