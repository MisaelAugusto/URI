# -*- coding: utf-8 -*-

A, B = map(int, input().split())

isMultiple = (A % B == 0) or (B % A == 0)

print("Sao Multiplos" if (isMultiple) else "Nao sao Multiplos")