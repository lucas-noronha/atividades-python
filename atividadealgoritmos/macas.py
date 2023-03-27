while True:
    qtdeComprada = int(input("Quantas vai levar? Se levar pelo menos 12 é 1 real cada, se levar menos é 1.30: "))

    valorCompra = int
    if qtdeComprada >= 12:
        valorCompra = qtdeComprada
    else:
        valorCompra = qtdeComprada * 1.3

    print("O valor total é: R$ ", valorCompra)