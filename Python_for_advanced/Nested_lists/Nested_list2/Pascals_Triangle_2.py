'''На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.'''
'''Sample Input 2:

5
Sample Output 2:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
n = int(input())
P=[]
for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=P[i-1][j-1]+P[i-1][j]
    P.append(row)

for r in P:
    print(*r)