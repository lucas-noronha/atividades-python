numeroConta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))

saldoAtual = saldo - debito + credito

print("A conta", numeroConta, "possui o saldo atual de:", saldoAtual)

if saldoAtual >= 0:
    print("Saldo positivo!")
else:
    print("Saldo negativo!")