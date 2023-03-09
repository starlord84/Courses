'''На вход программе подаются два натуральных числа nn и mm. Напишите программу, 
которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.'''
'''Sample Input 1:

3 7
Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21'''
s=input().split()
n=int(s[0])
m=int(s[1])
matrix=[[0 for i in range(m)] for _ in range(n)]
count =1
for i in range(m):
    for j in range(n):
        matrix[j][i] += count
        count+=1
for i in range(n):
    print(*matrix[i])