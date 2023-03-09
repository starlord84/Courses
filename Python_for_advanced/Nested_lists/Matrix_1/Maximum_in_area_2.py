'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
'''Sample Input 1:

3
1 4 5
6 7 8
1 1 6
Sample Output 1:

8
'''
n = int(input())
s = []

for i in range(n):
    f = [int(i) for i in input().split()]
    for j in range(len(f)):
        if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
            s.append(f[j])

print(max(s))