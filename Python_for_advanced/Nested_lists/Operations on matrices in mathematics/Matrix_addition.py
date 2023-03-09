'''Напишите программу для вычисления суммы двух матриц.'''
'''Sample Input 1:

2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3
Sample Output 1:

4 4 4 6
6 9 8 4'''
n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
a = input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix3[i][j] += matrix1[i][j] + matrix2[i][j]

for row in matrix3:
    print(*row)