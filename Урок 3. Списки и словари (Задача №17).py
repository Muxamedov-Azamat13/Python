# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

lst = [1, 1, 2, 0, -1, 3, 4, 4]
my_list = set(lst)
print(len(my_list))
