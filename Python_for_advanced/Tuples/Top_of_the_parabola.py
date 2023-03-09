'''Уравнение параболы имеет вид y =ax^2 + bx + cy =ax 
2
 +bx+c, где a \neq 0a

=0. Напишите программу, которая по введенным значениям a, b, ca,b,c определяет и выводит вершину параболы.'''
'''
Sample Input 1:

-2
6
1
Sample Output 1:

(1.5, 5.5)
'''
def coords(a, b, c):
    x = -(b / (2 * a))
    y = (4 * a * c - b**2) / (4 * a)
    return x, y

result = coords(int(input()), int(input()), int(input()))
print(result)
