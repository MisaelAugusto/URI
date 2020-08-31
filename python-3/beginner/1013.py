# -*- coding: utf-8 -*-

def MAX(A, B):
    return (A + B + abs(A - B)) / 2

A, B, C = map(int, input().split())

print("%d eh o maior" % (MAX(MAX(A, B), C)))