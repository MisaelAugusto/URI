# -*- coding: utf-8 -*-

N = int(input())

MONEY = [100, 50, 20, 10, 5, 2, 1]

print(N)
for i in range(7):
    print("%d nota(s) de R$ %d,00" % (N / MONEY[i], MONEY[i]))
    N = N % MONEY[i]