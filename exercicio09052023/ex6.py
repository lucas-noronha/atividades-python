vet = []
for i in range(20):
    vet.append(int(input("Digite um número: ")))

x = int(input("Digite o numero verificador: "))

vetB = []


if x in vet:
    print("entrou")
    for k in vet:
        if k != x:
            vetB.append(k)
    
    
print(vetB)