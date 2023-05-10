vetA = []

for i in range(10):
    vetA.append(int(input("Digite um valor: ")))

vetB = vetA[::-1]

vetN = []

for i in range(10):
    vetN.insert(i, (vetA[i] + vetB[i]))

print(vetN)