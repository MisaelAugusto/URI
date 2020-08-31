# -*- coding: utf-8 -*-

j, k = 0, 0
par, impar = [], []
for i in range(15):
  N = int(input())

  if (N % 2 == 0):
    par.append("par[%d] = %d" % (j % 5, N))
    j += 1
  else:
    impar.append("impar[%d] = %d" % (k % 5, N))
    k += 1

  if (len(par) == 5):
    print("\n".join(par))
    par = []

  if (len(impar) == 5):
    print("\n".join(impar))
    impar = []

print("\n".join(impar))
print("\n".join(par))