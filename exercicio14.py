# Laço de repetição
while True:
    tipo_venda = input("Digite a forma de pagamento. Ex.: Vista |  Prazo | Cartão : ").title()
    # se o tipo_venda for vista
    if tipo_venda == "Vista":
        print("Para pagamentos à Vista: desconto de 10%")
    # Se o tipo_venda for prazo
    elif tipo_venda == "Prazo":
        data = int(input("30, 60 ou 90 dias para o pagamento? "))
        if data == 30:
            print("Para pagamentos à Prazo em 30 dias: desconto de 5%")
        elif data == 60:
            print("Para pagamentos à Prazo em 60 dias: O preço permanece o mesmo")
        elif data == 90:
            print("Para pagamentos à Prazo em 90 dias: Acréscimo de 5%")
        else:
            print("Pagamentos à Prazo requerem que seja escolhido um prazo de 30, 60 ou 90 dias")
    # se o tipo_venda  for cartão
    elif tipo_venda == "Cartão":
        tipo_venda_cartao = input("Crédito ou Débito? ").title()
        if tipo_venda_cartao == "Débito":
            print("Para pagamentos com Cartão de Débito: Desconto de 8%")
        elif tipo_venda_cartao == "Crédito":
            print("Para pagamentos com Cartão de Crédito: Desconto de 7%")
        else:
            print("Apenas existem as opções de pagamento com Cartão de Débito ou Cartão de Crédito.")
    else:
        print("São aceitas apenas formas de pagamento à Vista,  Prazo e Cartão")

