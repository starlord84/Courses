'''На вход программе подаются два натуральных числа nn и mm. Напишите программу, 
которая создает матрицу размером n \times mn×m и заполняет её числами от 11 до n \cdot mn⋅m в соответствии с образцом.'''
'''Sample Input 1:

3 4
Sample Output 1:

1  2  3  4
5  6  7  8
9  10 11 12'''
n, m = map(int, input().split())
matrix = []
counter = 1

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(counter)
        counter += 1
        
        print(f'{matrix[i][j]}'.ljust(3), end='')
    print()