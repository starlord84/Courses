'''Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.'''
'''Sample Input 1:

3
0 1 2
1 2 3
2 3 4
Sample Output 1:

YES'''
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
    if flag == False:
        print('NO')
        break
else:
    print('YES')
