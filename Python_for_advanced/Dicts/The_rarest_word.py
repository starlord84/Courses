'''На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''
'''Sample Input 2:

home sweet home sweet.
Sample Output 2:

home'''
li = [word.strip(".,!?:;-").lower() for word in input().split()]
di = {word: li.count(word) for word in li}
m = min(di.values())

for k, v in sorted(di.items(), key=lambda t: t[0]):
    if v == m:
        print(k)
        break