# -*- coding: utf-8 -*-

day1 = int(input().split()[1])
hour1, minute1, second1 = map(int, input().split(" : "))

day2 = int(input().split()[1])
hour2, minute2, second2 = map(int, input().split(" : "))

totalSeconds1 = hour1 * 3600 + minute1 * 60 + second1
totalSeconds2 = hour2 * 3600 + minute2 * 60 + second2

days = day2 - day1

if (totalSeconds1 < totalSeconds2):
  seconds = totalSeconds2 - totalSeconds1
else:
  seconds = 86400 - totalSeconds1 + totalSeconds2
  days -= 1

print("%d dia(s)" % days)
print("%d hora(s)" % (seconds // 3600))
print("%d minuto(s)" % ((seconds % 3600) // 60))
print("%d segundo(s)" % ((seconds % 3600) % 60))