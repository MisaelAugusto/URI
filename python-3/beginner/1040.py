# -*- coding: utf-8 -*-

N1, N2, N3, N4 = map(float, input().split())

MEDIA = ((2 * N1) + (3 * N2) + (4 * N3) + N4) / 10
print("Media: %.1f" % MEDIA)

if (MEDIA >= 7.0):
    print("Aluno aprovado.")
elif (5.0 <= MEDIA < 7.0):
    NOTA = float(input())
    M_FINAL = (MEDIA + NOTA) / 2
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % NOTA)
    print("Aluno %s." % ("aprovado" if (M_FINAL > 5.0) else "reprovado"))
    print("Media final: %.1f" % M_FINAL)
else:
    print("Aluno reprovado.")