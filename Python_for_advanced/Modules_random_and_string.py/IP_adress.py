'''IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.'''
import random
def generate_ip():
    res, a = '', 0
    for i in range(4):
        a = str(random.randint(0, 255)) + '.'
        res += a
    return res[:-1]
print(generate_ip())