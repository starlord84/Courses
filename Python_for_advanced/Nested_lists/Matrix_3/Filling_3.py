'''На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.'''
'''Sample Input 1:

5
Sample Output 1:

1  0  0  0  1
0  1  0  1  0
0  0  1  0  0
0  1  0  1  0
1  0  0  0  1'''
n = int(input())

matrix = []
for i in range(n):
    ii = n - i - 1
    row = [1 if i == j or ii == j else 0 for j in range(n)]
    matrix.append(row)
    
for row in matrix:
    print(*row)