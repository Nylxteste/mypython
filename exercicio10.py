
#  Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7),
#  Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).

# Declarações
resultado = 0
notas = []
nome = 'gil' #input("Digite seu nome: ").title()



for i in range(3):
    notas.append(float(input(f"Digite a {i+1} nota")))
    resultado += notas[i]

resultado = resultado / 3
# Decisão de aprovação do colocado
if resultado >= 7:
    print(len(notas))
    print(f"""{nome},
    Aprovado,
    Média: {resultado:.2f}""")
# Decisão de reprovação do colocado
elif resultado <= 5:
    print(len(notas))
    print(f"""{nome},
    Reprovado,
    Média: {resultado:.2f}""")
# Decisão de recuperação do colocado
else:
    print(len(notas))
    print(f"""{nome},
    Recuperação,
    Média: {resultado:.2f}""")

