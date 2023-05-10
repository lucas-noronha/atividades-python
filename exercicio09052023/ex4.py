vetA = []

for i in range(10):
    vetA.append(int(input("Digite um valor: ")))

x = int(input("Digite o multiplicador"))

vetM = []

for k in vetA:
    vetM.append(k * x)

print(vetM)
