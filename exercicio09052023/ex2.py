listaNotas = []
for i in range(20):
    listaNotas.append(input(f"Digite a nota do aluno {i + 1}: "))


somaNotasTurma = 0
for nota in listaNotas:
    somaNotasTurma += int(nota)

mediaTurma = somaNotasTurma / len(listaNotas)
qtdeAlunosAcimaMedia = 0

for nota in listaNotas:
    if int(nota) > mediaTurma:
        qtdeAlunosAcimaMedia += 1

print(f'A nota média da turma foi: {mediaTurma}\nQuantidade de alunos acima da média: {qtdeAlunosAcimaMedia}')

