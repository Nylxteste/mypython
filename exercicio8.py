# Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior.

num1 = float(input('Digite o número para validação: '))
num2 = float(input('Digite o número para validação: '))

if num1 > num2:
    print(f"O primeiro número digitado; {num1}, é maior que o segundo número digitado; {num2}. ")
elif num1 == num2:
    print(f"Os números digitados são iguais, ou seja, tem o mesmo valor. ")
else:
    print(f"O Segundo número digitado; {num2}, é maior que o primeiro número digitado; {num1}")