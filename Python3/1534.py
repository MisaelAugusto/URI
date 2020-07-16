# -*- coding: utf-8 -*-

while (True):
   try :
      N = int(input())

      answer = []
      for i in range(N):
        answer.append([3] * N)
      
      for i in range(N):
        for j in range(N):
          if (i == j):
            answer[i][j] = 1

          if (i + j == N - 1):
            answer[i][j] = 2

      for i in range(N):
        print("".join(map(str, answer[i])))

   except EOFError:
      break