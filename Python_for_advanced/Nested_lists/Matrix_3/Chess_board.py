'''На вход программе подаются два натуральных числа nn и mm. 
Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке. 
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, 
разделяя элементы пробелами.'''
'''Sample Input 1:

3 4
Sample Output 1:

. * . *
* . * .
. * . *'''
x, y = [int(i) for i in input().split()]

matrix = [['.'] * y for _ in range(x)]

for i in range(x):
    if i == 0 or i % 2 == 0:
        for j in range(1, y, 2):
            matrix[i][j] = '*'
    else:
        for j in range(0, y, 2):
            matrix[i][j] = '*'

for row in matrix:
    print(*row)
