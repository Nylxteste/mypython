numeros = []


while len(numeros) < 3:
    numeros.append(int(input("Digite seu número")))

for u in range(len(numeros)-1):
    for i in range(len(numeros)-1):
        if numeros[i] > numeros[i+1]:
            aux = numeros[i]
            numeros[i] = numeros[i+1]
            numeros[i+1] = aux

print(numeros)