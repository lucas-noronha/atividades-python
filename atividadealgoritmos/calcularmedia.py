notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))

resultado = (notaUm + notaDois) / 2

if resultado >= 6:
    print("O aluno foi aprovado! Nota:", resultado)
else:
    print("O aluno foi reprovado!: Nota:", resultado)