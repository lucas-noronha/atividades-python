Q = []

i = 0
while i < 20:
    valor = int(input("Digite um valor positivo: "))
    if valor > 0:
        Q.append(valor)
        i += 1
    else:
        print("Digite apenas números positivos")


maior = Q[0]
posicao = 0

for index in range(len(Q)):
    if Q[index] > maior:
        maior = Q[index]
        posicao = index

print(f"O maior elemento é {maior} e sua posição é {posicao}")