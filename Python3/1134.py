# -*- coding: utf-8 -*-

dic = { 1: 0, 2: 0, 3: 0 }
while (True):
  option = int(input())
  
  if (not(option in [1, 2, 3, 4])):
    continue

  if (option == 4):
    break

  dic[option] += 1


print("MUITO OBRIGADO")
print("Alcool: %d" % dic[1])
print("Gasolina: %d" % dic[2])
print("Diesel: %d" % dic[3])