# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())

ANSWER1 = (B > C) and (D > A) and ((C + D) > (A + B))
ANSWER2 = (C > 0) and (D > 0) and (A % 2 == 0)

print("Valores aceitos" if (ANSWER1 and ANSWER2) else "Valores nao aceitos")