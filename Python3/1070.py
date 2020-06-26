# -*- coding: utf-8 -*-

X = int(input())
start = X if(X % 2 != 0) else X + 1

result = range(start, start + 12, 2)

for number in result:
  print(number)