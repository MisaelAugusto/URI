# -*- coding: utf-8 -*-

N = float(input())

MONEY = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for i in range(6):
    print("%d nota(s) de R$ %d.00" % (N / MONEY[i], MONEY[i]))
    N %= MONEY[i]

N *= 100
CENTS = [100, 50, 25, 10, 5, 1]
CENTS_TEXT = ["1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]

print("MOEDAS:")
for i in range(6):
    print("%d moeda(s) de R$ %s" % (N // CENTS[i], CENTS_TEXT[i]))
    N %= CENTS[i]