# Declarações

semana = {
    'Segunda':1 ,
    'Terça':2,
    'Quarta':3,
    'Quinta':4,
    'Sexta':5,
    'Sabado':6,
    'Domingo':7
}

# Entrada de informação
data = int(input("Digite o dia da semana: "))

while data >= 8:
    data -= 7

for key, value in semana.items():
    if data == value :
        print(f"A data {value} é {key}")