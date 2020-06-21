"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random

gen_list = [random.randint(1, 1000) for _ in range (50)]
#gen_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

item_prev = gen_list[0]
rez_list = []
for item in gen_list:
    if item > item_prev:
        rez_list.append(item)
        item_prev = item
    else:
        item_prev = item

rez_list2 = [param for number, param in enumerate (gen_list) if param > gen_list[number-1] and param != gen_list[0]]


print ("Исходный список")
print (gen_list)
print ("Отсортированный список")
print (rez_list)
print ("Отсортированный список_2")
print (rez_list2)
