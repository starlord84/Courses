'''Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы.
 Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).'''
'''
Sample Input 4:

3
Sample Output 4:

[1, 3, 3, 1]
'''
n = int(input())
s = []
for i in range(n+1):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=i and j!=0: row[j] = s[i-1][j-1]+s[i-1][j]
    s.append(row)
print(s[n] if n!=0 else [1])