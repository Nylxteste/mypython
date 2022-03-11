#Faça um algoritmo para ler um salário e atualizá-lo de acordo com a tabela abaixo.

# Entrada de dados do usuário
salario = float(input("Digite o valor de seu salário: "))

# Decisão para aumento salariál

# se 600 ou menos
if salario <= 600:
    salario = salario * 1.3 # O salário é incrementado em 30%
elif salario <= 1100:
    salario = salario * 1.25 # O salário é incrementado em 25%
elif salario <= 2400:
    salario = salario * 1.20 # O salário é incrementado em 20%
elif salario <= 3550:
    salario = salario * 1.15 # O salário é incrementado em 15%
else:
    salario = salario * 1.1 # O salário é incrementado em 10%
print(salario)