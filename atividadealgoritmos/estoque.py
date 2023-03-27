qtdeAtual = int(input("Digite a quantidade atual em estoque: "))
qtdeMax = int(input("Digite a quantidade máxima em estoque: "))
qtdeMin = int(input("Digite a quantidade mínima em estoque: "))


qtdeMedia = (qtdeMax + qtdeMin) / 2
print("A quantidade média de produtos é:", qtdeMedia)

if qtdeAtual >= qtdeMedia:
    print("Não efetuar compra!")
else:
    print("Efetuar compra!")
