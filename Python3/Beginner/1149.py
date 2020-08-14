# -*- coding: utf-8 -*-

numbers = list(map(int, input().split()))

answer = sum(range(numbers[0], numbers[0] + numbers[-1]))

print(answer)