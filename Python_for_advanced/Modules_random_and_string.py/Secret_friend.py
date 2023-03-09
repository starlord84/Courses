'''Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.'''
'''Sample Input 1:

3
Светлана Зуева
Аркадий Белых
Борис Боков
Sample Output 1:

Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых'''

from random import *
fri = [input() for _ in range(int(input()))]
fricop = fri.copy()
a = 0
def rand(a, b):
	r = 0
	for i, j in zip(a, b):
		if i!=j:
			r+=1
	return r
while a != len(fri):
	shuffle(fricop)
	a = rand(fri, fricop)
for k, l in zip(fri, fricop):
	print(k,'-',l)