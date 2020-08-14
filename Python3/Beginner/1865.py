# -*- coding: utf-8 -*-

C = int(input())

for i in range(C):
  name, _ = input().split()

  print("Y" if (name == "Thor") else "N")