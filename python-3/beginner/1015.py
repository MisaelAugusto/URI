# -*- coding: utf-8 -*-

X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())

DISTANCE = ( (X2 - X1)**2 + (Y2 - Y1)**2 ) ** (0.5)

print("%.4f" % (DISTANCE))