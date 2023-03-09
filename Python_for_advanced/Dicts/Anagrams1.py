'''Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). 
Например, английские слова evil и live – это анаграммы.'''
'''Sample Input 1:

thing
night
Sample Output 1:

YES'''
s = sorted(input())
dct1 = dict(zip(range(len(s)), s))

s = sorted(input())
dct2 = dict(zip(range(len(s)), s))

print('YES' if dct1 == dct2 else 'NO')