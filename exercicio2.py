a = int(input("Digite o primeiro valor: "))

b = int(input("Digite o segundo valor: "))

if a > b:
    print(a,b)
elif b > a:
    print(a,b)
    aux = a
    a = b
    b = aux
else:
    print(f"Os valores inseridos são iguais {a,b}")