"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

numb_list = [param for param in range(20, 240) if param % 20 == 0 or param % 21 == 0]

print (numb_list)