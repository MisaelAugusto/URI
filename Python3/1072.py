# -*- coding: utf-8 -*-

N = int(input())

inn, out = 0, 0
for i in range(N):
  X = int(input())
  if (10 <= X <= 20):
    inn += 1
  else:
    out += 1

print("%d in" % inn)
print("%d out" % out)
