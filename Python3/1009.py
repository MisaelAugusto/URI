# -*- coding: utf-8 -*-

NAME = input()
SALARY = float(input())
SALES = float(input())

TOTAL = SALARY + 0.15 * SALES

print("TOTAL = R$ %.2f" % (TOTAL))