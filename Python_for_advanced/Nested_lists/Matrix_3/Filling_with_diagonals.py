'''На вход программе подаются два натуральных числа nn и mm. Н
апишите программу, которая создает матрицу размером n \times mn×m заполнив её "диагоналями" в соответствии с образцом.'''
'''Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15'''
n, m = [int(i) for i in input().split()]
mtx = [[0] * m for _ in range(n)]
sequence, k = 1, 0

while sequence != n * m + 1:
    for i in range(n):
        for j in range(m):
            if i + j == k:
                mtx[i][j] = sequence
                sequence += 1
    k += 1

for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(3), end='')
    print()
