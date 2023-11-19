# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input('Введите число Фибоначчи: '))
fib_prev, fib_next = 0, 1
count = 2
while a > fib_next:
    fib_prev, fib_next = fib_next, fib_prev + fib_next
    count += 1
if a == fib_next:
    print(count)
else:
    print('-1')
