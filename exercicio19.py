

def relacao (n1,n2):
    if n1 == n2:
        print("Números iguais")
    elif n1 >= n2:
        print("Primeiro é maior")
    else:
        print("Segundo é maior")

teste = relacao(input("Digite o primeiro número: "),input("Digite o segundo número: "))