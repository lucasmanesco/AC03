qtd_alunos = int(input())
notas_original = []
notas_atividade = []

while len(notas_original) < qtd_alunos:
    nota1 = float(input())
    notas_original.append(nota1)

while len(notas_atividade) < qtd_alunos:
    nota2 = float(input())
    notas_atividade.append(nota2)

notas_alteradas = 0

aluno = 0
notas_final = []

while len(notas_final) < qtd_alunos:
    if notas_original[aluno] < 10 and notas_atividade[aluno] == 10:
        nota3 = notas_original[aluno] + 2
        if nota3 >= 10:
            nota3 = 10
        notas_alteradas += 1
    else:
        nota3 = notas_original[aluno]
    notas_final.append(nota3)
    aluno += 1

print('NOTAS ALTERADAS:', notas_alteradas)

for i in range(0, qtd_alunos):
    if notas_original[i] == notas_final[i]:
        print(f'-({i+1:03d}) original: {notas_original[i]:0>5.2f} | final: {notas_final[i]:0>5.2f}')
    else:
        print(f'*({i+1:03d}) original: {notas_original[i]:0>5.2f} | final: {notas_final[i]:0>5.2f}')