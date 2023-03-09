'''Напишите программу, которая меняет местами столбцы в матрице.'''
'''Sample Input 1:

3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
Sample Output 1:

12 11 13 14
22 21 23 24
32 31 33 34'''
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]
change = [int(i) for i in input().split()]
a, b = change[0], change[1]

for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

for row in matrix:
    print(*row)