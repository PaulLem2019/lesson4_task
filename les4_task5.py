"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех
элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

def mult_funct(numb_1, numb):
    return numb_1*numb

gen_list = [param for param in range (100, 1001) if param % 2 == 0]

print ("Иcходный список")
print (gen_list)
print ("Результат")
make_rez = reduce(mult_funct, gen_list)
print (make_rez)

