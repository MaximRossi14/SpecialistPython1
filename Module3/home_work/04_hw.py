# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]


import random
numbers = []
new_numbers = []
spisok = []
n = int(input())
for i in range(n):
    numbers.append(random.randint(-10, 30))
    if numbers[i] >= 0:
        new_numbers.append(numbers[i]**0.5)

for i in range(len(new_numbers)):
    if new_numbers[i] % 1 == 0:
        spisok.append(int(new_numbers[i]))
print(numbers)
print(spisok)
