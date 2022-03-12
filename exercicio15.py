
while True:
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    num3 = int(input("digite o 3º número: "))
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    else:
        print("Ocorreu algum erro, digite os números novamente.")