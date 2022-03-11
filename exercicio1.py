
# entrada de valor
valor = int(input("Digite o valor inteiro a ser verificado: "))

# decisão, se o resto do valor dividido por 2 for 0 é par
if valor%2 == 0:
    print(f"O número '{valor}' é par")
# Se for diferente de 0 é impar
else:
    print(f"O número '{valor}' é impar")