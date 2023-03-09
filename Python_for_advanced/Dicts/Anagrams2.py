'''На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
 Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.'''
'''Sample Input 1:

Вижу зверей
Живу резвей
Sample Output 1:

YES'''
s = sorted(s for s in input().lower() if s.isalpha())
dct1 = dict(zip(range(len(s)), s))
s = sorted(s for s in input().lower() if s.isalpha())
dct2 = dict(zip(range(len(s)), s))

print('YES' if dct1 == dct2 else 'NO')