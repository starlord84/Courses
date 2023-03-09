'''Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, 
Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.'''
import random as r
import string

def generate_index():
    S = string.ascii_uppercase
    ind = (''.join(r.sample(S, 2)) + str(r.randrange(100))
    + "_" + str(r.randrange(100)) + ''.join(r.sample(S, 2)))
    return ind