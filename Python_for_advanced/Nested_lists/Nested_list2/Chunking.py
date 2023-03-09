'''На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.'''
'''
Sample Input 4:

a b c d e f r g b
2
Sample Output 4:

[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
'''
def chunked(st, n):
    st = st.split()
    a = [[] for _ in range(0, len(st), n)]
    for i in range(len(a)):
        a[i].extend(st[:n])
        st = st[n:]
    return a

string = input()
num = int(input())

print(chunked(string, num))