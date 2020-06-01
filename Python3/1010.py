# -*- coding: utf-8 -*-

PROD1 = input().split()
PROD2 = input().split()

TOTAL = int(PROD1[1]) * float(PROD1[2]) + int(PROD2[1]) * float(PROD2[2])

print("VALOR A PAGAR: R$ %.2f" % (TOTAL))