'''Вам дан словарь, состоящий из пар слов-синонимов. 
Повторяющихся слов в словаре нет. Напишите программу,
 которая для одного данного слова определяет его синоним.'''
'''Sample Input 1:

4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:

Beautiful'''
lovar=dict([[i for i in input().split(' ')] for i in range(int(input()))])
a=input()
for key,value in lovar.items():
    if key==a:
        print(value)
    if value==a:
        print(key)