'''На вход программе подаются два натуральных числа nn и mm. 
Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "змейкой" в соответствии с образцом.'''
'''Sample Input 1:

3 5
Sample Output 1:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15'''
s=input().split()
n=int(s[0])
m=int(s[1])
matrix=[[0 for i in range(m)] for _ in range(n)]
count =1
for i in range(n):
    for j in range(m):
        matrix[i][j] += count
        count+=1
for i in range(n):
    if i%2==0:
        print(*matrix[i])
    else:
        matrix[i].reverse()
        print(*matrix[i])
