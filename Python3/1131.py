# -*- coding: utf-8 -*-

grenais, inter, gremio, draw = 0, 0, 0, 0

while (True):
  i, g = map(int, input().split())

  if (i > g):
    inter += 1
  elif (i < g):
    gremio += 1
  else:
    draw += 1

  grenais += 1

  option = int(input("Novo grenal (1-sim 2-nao)\n"))
  if (option == 2):
    break

print("%d grenais" % grenais)
print("Inter:%d"% inter)
print("Gremio:%d" % gremio)
print("Empates:%d" % draw)

if (inter > gremio):
  print ("Inter venceu mais")
elif (inter < gremio):
  print("Gremio venceu mais")
else:
  print("Não houve vencedor")