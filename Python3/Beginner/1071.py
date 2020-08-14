# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())

start = Y + 2 if (Y % 2 != 0) else Y + 1

result = sum(range(start, X, 2))

print(result)