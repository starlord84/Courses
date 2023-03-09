'''На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем nn строк по mm целых чисел в каждой,
 отделенных символом пробела.
Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.'''
'''
Sample Input 1:

3
4
0 3 2 4
2 3 5 5
5 1 2 3
Sample Output 1:

1 2'''
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row,col = i, j
            
print(row, col)
