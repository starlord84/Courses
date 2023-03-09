'''Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.'''
'''Sample Input 1:

4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6
Sample Output 1:

3 4 5 6
8 6 4 2
5 6 7 8
1 2 3 4'''
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
for row in matrix:
    print(*row)