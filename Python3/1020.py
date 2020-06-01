# -*- coding: utf-8 -*-

DAYS = int(input())

print("%d ano(s)" % (DAYS / 365))
print("%d mes(es)" % ((DAYS % 365) / 30))
print("%d dia(s)" % ((DAYS % 365) % 30))