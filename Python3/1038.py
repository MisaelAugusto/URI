# -*- coding: utf-8 -*-

X, Y = map(int, input().split())
TABLE = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

TOTAL = TABLE[X] * Y

print("Total: R$ %.2f" % TOTAL)