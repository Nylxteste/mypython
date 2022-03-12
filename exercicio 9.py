# Programa de declaração de um valor que está entre 100 e 200

# Declarações

valor = float(int(input("Digite o valor a ser validado: ")))

if valor >= 100 and valor <= 200:
     print(f"O valor digitado |> {valor} <| está DENTRO da faixa de ( 100 ~ 200 ) ")
else:
    print(f"O valor digitado |> {valor} <| está FORA da faixa de ( 100 ~ 200 ) ")