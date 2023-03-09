'''На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.'''
'''Sample Input 1:

5
Sample Output 1:

1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1'''
n = int(input())

for i in range(n):
    result =[]
    for j in range(n):
        if (i >= j and i >= n - 1 - j) or (i <= j and i <= n - 1 - j):
            result.append(1)
        else:
            result.append(0)
    print(*result)