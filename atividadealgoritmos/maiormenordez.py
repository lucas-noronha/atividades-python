while True:
    numero = float(input("Digite qualquer número: "))

    if numero > 10:
        print("O número informado é maior que 10. Valor digitado:", numero)
    elif numero < 10:
        print("O número informado é menor que 10. Valor digitado:", numero)
    else:
        print("O número é igual a 10. Valor digitado:", numero)