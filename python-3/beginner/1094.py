# -*- coding: utf-8 -*-

N = int(input())

dic = { 'C': 0, 'R': 0, 'S': 0 }

for i in range(N):
  amount, animal = input().split()

  dic[animal] += int(amount)

total = dic['C'] + dic['R'] + dic['S']

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % dic['C'])
print("Total de ratos: %d" % dic['R'])
print("Total de sapos: %d" % dic['S'])

print("Percentual de coelhos: %.2f %%" % (dic['C'] * 100 / total))
print("Percentual de ratos: %.2f %%" % (dic['R'] * 100 / total))
print("Percentual de sapos: %.2f %%" % (dic['S']* 100 / total))
