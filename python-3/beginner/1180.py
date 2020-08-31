# -*- coding: utf-8 -*-

N = int(input())
numbers = list(map(int, input().split()))

print("Menor valor: %d" % min(numbers))
print("Posicao: %d" % (numbers.index(min(numbers))))