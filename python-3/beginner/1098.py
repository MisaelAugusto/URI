# -*- coding: utf-8 -*-

I, J = 0, 1
for i in range(11):
  if (i % 5 == 0):
    print("I=%d J=%d" % (round(I), round(J)))
    print("I=%d J=%d" % (round(I), round(J + 1)))
    print("I=%d J=%d" % (round(I), round(J + 2)))
  else:
    print("I=%.1f J=%.1f" % (I, J))
    print("I=%.1f J=%.1f" % (I, J + 1))
    print("I=%.1f J=%.1f" % (I, J + 2))

  I += 0.2
  J += 0.2