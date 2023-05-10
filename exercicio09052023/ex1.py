listaClubes = []
for i in range(10):
    listaClubes.append(input("Digite o nome do seu time: "))

clubePesquisa = input("Qual clube deseja pesquisar: ")



if clubePesquisa in listaClubes:
    print("ACHEI")
else:
    print("NÃO ACHEI")