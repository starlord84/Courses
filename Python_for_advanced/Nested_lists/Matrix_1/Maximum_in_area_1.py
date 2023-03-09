'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
'''Sample Input 1:

3
1 4 5
6 7 8
1 1 6
Sample Output 1:

7'''
n = int(input())
arr = []
mtr = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i >= j:
            arr.append(mtr[i][j])
print(max(arr))