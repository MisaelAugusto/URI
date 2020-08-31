# -*- coding: utf-8 -*-

A, B, C = map(float, input().split())
PI = 3.14159

print("TRIANGULO: %.3f" % (A * C / 2))
print("CIRCULO: %.3f" % (PI * C**2))
print("TRAPEZIO: %.3f" % ((A + B) * C / 2))
print("QUADRADO: %.3f" % (B ** 2))
print("RETANGULO: %.3f" % (A * B))