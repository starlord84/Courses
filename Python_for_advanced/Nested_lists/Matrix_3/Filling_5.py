'''На вход программе подаются два натуральных числа nn и mm. 
Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.'''
'''Sample Input 1:

5 5
Sample Output 1:

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4'''
n, m = [int(num) for num in input().split()]
matrix = [num for num in range(1, m + 1)]
for i in range(n):
    for j in range(m):
        print(matrix[j], end=' ')
    pop = matrix.pop(0)
    matrix.append(pop)
    print()