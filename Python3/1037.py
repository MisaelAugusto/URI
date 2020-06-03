# -*- coding: utf-8 -*-

NUMBER = float(input())

if (0 <= NUMBER <= 25):
    ANSWER = "Intervalo [0,25]"
elif (25 < NUMBER <= 50):
    ANSWER = "Intervalo (25,50]"
elif (50 < NUMBER <= 75):
    ANSWER = "Intervalo (50,75]"
elif (75 < NUMBER <= 100):
    ANSWER = "Intervalo (75,100]"
else:
    ANSWER = "Fora de intervalo"

print(ANSWER)
    