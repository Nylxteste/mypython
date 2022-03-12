
# Declarações

txt = "O atleta: {} se encontra na categoria: {}"
nome = input("Digite o nome do atleta: ").title()

idade = int(input("Digite a idade do atleta: "))

if idade >= 5 and idade <= 10:
    print(txt.format(nome,"Infantil"))
elif idade >= 11 and idade <= 15:
    print(txt.format(nome,"Juvenil"))
elif idade >= 16 and idade <= 20:
    print(txt.format(nome,"Junior"))
elif idade >= 21 and idade <= 25:
    print(txt.format(nome,"Profissional"))
else:
    print("A idade do atleta não está dentro de alguma categoria.")






