vet = []
for i in range(30):
    vet.append(int(input("Digite um número: ")))

x = int(input("Digite o numero verificador"))

contador = 0
for i in vet:
    if i == x:
        contador += 1

print(contador)