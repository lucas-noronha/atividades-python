vetA = []

for i in range(10):
    vetA.append(int(input("Digite um numero: ")))


dicionario = {}
for i in range(len(vetA)):
    for j in range(len(vetA)):
        if vetA[i] == vetA[j] and j != i and j > i:
            dicionario[f'duplicidade-{i}'] = { "valor": vetA[j], "posicoes": f'{i},{j}'}
    
for k in dicionario:
    print(dicionario[k])