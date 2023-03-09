'''Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.'''
'''
Sample Input 1:

4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5
Sample Output 1:

2
1
2
1
'''

n = int(input())
l = [input().split() for _ in range(n)]
counter = 0
for i in l:
    sr = (sum(list(map(int, i)))) / len(i)
    for j in i:
        if int(j) > sr:
            counter += 1
    print(counter)
    counter = 0
