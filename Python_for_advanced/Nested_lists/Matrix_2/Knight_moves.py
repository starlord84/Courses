'''На шахматной доске 8×8 стоит конь. 
Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, 
отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.'''
'''
Sample Input 1:

b6
Sample Output 1:

* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .'''
# put your python code here
col, row = input().strip()
coor_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
arr = [["N" if [i, j] == [coor_row[row], coor_col[col]] else '.' for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        if (coor_row[row] - i) * (coor_col[col] - j) in [-2, 2]: arr[i][j] = "*" 
for line in arr:
    print(*line, sep = ' ')