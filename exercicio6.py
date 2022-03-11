# De acordo com a tabela abaixo, desenvolva um algoritmo que leia um código do produto informado
# pelo usuário e informe a descrição do lanche.

# Declarações

vetorzinho = []    # vetor para coleta das keys do dict
vet =[]     # vetor para coleta dos values do dict
count = 0   # count necessário para iteração e verificação do input em relação aos vetores
flag_nao = False     # flag utilizada para sinalização não seja localizado um valor relativo ao pedido

# Dicionário informando os valores e chaves
lanches = {
    '100' : 'Pão com manteiga na chapa com café com leite.',
    '200' : 'Hot dog com suco de laranja.',
    '300' : 'Sanduiche natural com suco de uva.',
    '400' : 'Misto Quente com fanta laranja.',
    '500' : 'Pão com manteiga com café.',
    '600' : 'Pão com manteiga na chapa com café com leite.'
}

# Entrada de dados do usuário
pedido = input("Digite o número do pedido: ")

# laço de repetição utilizado para coleta das chaves e valores em seus determinados vetores
for key, value in lanches.items():
    vetorzinho.append(key)
    vet.append(value)


# laço de repetição que, enquanto count for menor que o tamanho da variável vetorzinho ocorre a  iteração
while count < len(vetorzinho):
    count += 1     # incremento do count a cada iteração
    if pedido == vetorzinho[count-1]:
        print(vet[count-1])
        flag_nao = True     # caso o pedido seja igual o indice determinado pelo count em vetorzinho, a flag é determinada como true
        break      # parada da situação

# Decisão, se a flag não for verdadeiro, irá informar ao usuário que o código informado é invalido.
if not flag_nao:
    print("Código informado inválido.")

# Fim do programa