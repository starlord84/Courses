'''Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.'''
'''Sample Input 1:

4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4
Sample Output 1:

Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
'''
n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
left =  sum([sum([matrix[i][j] for j in range(n) if i > j and i < n-1-j]) for i in range(n)])
down =  sum([sum([matrix[i][j] for j in range(n) if i > j and i > n-1-j]) for i in range(n)])
up =    sum([sum([matrix[i][j] for j in range(n) if i < j and i < n-1-j]) for i in range(n)])
right = sum([sum([matrix[i][j] for j in range(n) if i < j and i > n-1-j]) for i in range(n)])

print(f"""Верхняя четверть: {up}
Правая четверть: {right}
Нижняя четверть: {down}
Левая четверть: {left}""")