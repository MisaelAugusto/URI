# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())

start, end = min(X, Y), max(X, Y)
firstDivisible = start if (start % 13 == 0) else start + (13 - (start % 13))

answer = sum(range(start, end + 1)) - sum(range(firstDivisible, end + 1, 13))

print(answer)