'''Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.'''
'''Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 4 1 
8 5 2 
9 6 3 '''
n=int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for j in range(n):
    for i in range(n-1, -1, -1):
        print(matrix[i][j], end = ' ')
    print()