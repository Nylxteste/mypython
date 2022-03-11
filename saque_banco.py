# Declarações
count = 0

nota = 200

# Entrada de dados solicitando a inserção do valor de saque
saque = int(input("Digite o valor a ser retirado: R$"))

if saque > 0:
    print('''O saque foi efetuado com sucesso.
Foi retirado:''')
    # Laço de iteração enquanto o valor de saque for diferente de 0
    while saque != 0:
        count += 1
        saque -= nota
        if nota > saque:
            print(f"{count} nota de R${nota}")
            if nota > saque:
                nota = 100
                count = 0
                if nota > saque:
                    nota = 50
                    count = 0
                    if nota > saque:
                        nota = 20
                        count = 0
                        if nota > saque:
                            nota = 10
                            count = 0
                            if nota > saque:
                                nota = 1
                                count = 0
else:
    print(f"O valor digitado R${saque} é negativo, e por este motivo o saque será cancelado.")
    