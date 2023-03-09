'''На вход программе подается строка текста, содержащая символы. 
Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.'''
'''Sample Input 2:

w w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2:

[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], 
['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]'''
res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)