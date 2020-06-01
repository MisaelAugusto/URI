# -*- coding: utf-8 -*-

N = int(input())

HOURS = N // 3600
MINUTES = (N % 3600) // 60
SECONDS = (N % 3600) % 60

print("%d:%d:%d" % (HOURS, MINUTES, SECONDS))