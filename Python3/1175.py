# -*- coding: utf-8 -*-

answer = []
for i in range(20):
  Y = int(input())
  answer = [Y] + answer

for i in range(20):
  print("N[%d] = %d" % (i, answer[i]))
