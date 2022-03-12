# Elabore um algoritmo para testar se uma senha digita é igual a “batatafrita”.
# Se a senha estiver correta escreva “Acesso permitido”,
# do contrário emita a mensagem “Você não tem acesso ao sistema”.

# laço de iteração enquanto verdade
while True:
    senha = input("Digite sua senha: ")
    # Se a senha for igual "batatafrita" o laço de iteração irá encerrar.
    if senha == "batatafrita":
        print("Acesso permitido")
        break
    # Se a senha não for igual a "batatafrita" o laço de iteração irá continuar.
    else:
        print("Você não tem acesso ao sistema")
