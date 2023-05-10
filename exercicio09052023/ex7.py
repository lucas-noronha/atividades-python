vet = []
for i in range(10):
    vet.append(int(input("Digite um número: ")))

print("Próximo vetor")

vetB = []
for i in range(10):
    vetB.append(int(input("Digite um número: ")))

contadorIguais = 0

for i in range(len(vet)):
    a = vet[i]
    for j in range(len(vetB)):
        b = vetB[j]
        if a == b and i == j:
            contadorIguais += 1

print(contadorIguais)