'''Напишите программу, которая выводит список хорошистов и отличников в классе.'''
'''Sample Input 1:

3
Гуев 3
Чаниев 5
Барсуков 2
Sample Output 1:

Гуев 3
Чаниев 5
Барсуков 2

Чаниев 5'''
lst = [input().split() for i in range(int(input()))]
    
for i in range(len(lst)):
    print(lst[i][0], lst[i][1])

print()

for i in range(len(lst)):
    if lst[i][1] in '45':
        print(lst[i][0], lst[i][1])