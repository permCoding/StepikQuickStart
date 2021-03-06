# на Питоне не ве тесты прохдят по времени

s, n = map(int, input().split())
w = [0]+list(map(int,input().split()))

z = []
for i in range(n+1):
	z.append([0]*(s+1))

z[0][0] = 1
for i in range(1,n+1):
	for j in range(0, s+1):
		if w[i] <= j:
			z[i][j] = max(z[i-1][j],z[i-1][j-w[i]])
		else:
			z[i][j] = z[i-1][j]

for j in range(s,-1,-1):
	if z[n][j] > 0:
		r = j
		break
print(r)
'''
Рюкзак
У вас есть n слитков золота, каждый имеет свой вес.
Также у вас есть рюкзак вместимости S.
Необходимо вычислить максимальный вес, который вы можете с собой унести.
--- Вы НЕ можете дробить слитки. ---

Входные данные
В первой строке записано два целых числа S и N (1<=S<=10^4; 1<=N<=300).
Во второй строке записаны n целых чисел - веса слитков.
Каждый слиток имеет неотрицательный вес, не превосходящий 10^5.

Выходные данные
Выведите единственное число - максимальный суммарный вес, который вы можете унести.

Sample Input 1:
10 6
2 3 4 4 6 9
Sample Output 1:
10
Sample Input 2:
10 6
1 1 1 1 1 1
Sample Output 2:
6
'''
