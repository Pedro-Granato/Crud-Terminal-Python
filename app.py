# fazer um CRUD simples no terminal
# CREATE -> cadastrar usuários em uma lista ou dicionário
# READ -> ler as informções e exibir na tela
# UPDATE -> mudar o cadastro de um usuário pelo seu id/etc
# DELETE -> deletar usuário da lista/dicionário
import os
import time

usuarios = []


def cadastrarUsuario():
    nome_usuario = input("Informe o nome:  ")
    idade_usuario = input("Informe a idade: ")
    email_usuario = input("Informe o email: ")
    telefone_usuario = input("Informe o telefone: ")
    genero_usuario = input("Informe o gênero: ")

    if not usuarios:  # retorna true se a lista estiver vazia
        novo_id = 1
    else:
        novo_id = usuarios[-1]["id"] + 1

    usuarios.append({
        "id": novo_id,
        "nome": nome_usuario,
        "idade": idade_usuario,
        "email": email_usuario,
        "telefone": telefone_usuario,
        "genero": genero_usuario
    })


def listarUsuarios():
    print("==== LISTA DE USUÁRIOS ====")
    for user in usuarios:
        print(f"Id: {user['id']} \n Nome: {user['nome']} \n Idade: {user['idade']} \n Email: {user.get('email', 'Nenhum')} \n Telefone: {user['telefone']}")
        print("==================")


def atualizarUsuarios():
    print("====Editor de Cadastro====")
    try:
        idAtualizar = int(
            input("\nInforme o Id do usuário a ser atualizado: "))
        if not idAtualizar.is_integer()
        usuario_encontrado = None

        for user in usuarios:  # percorre os usuarios
            # encontra o usuário desejado comparando o id de cada elemento da lista com o id do usuário que será atualizado
            if user['id'] == idAtualizar:
                usuario_encontrado = user
                break

        if not usuario_encontrado:
            print("Usuário não encontrado")
            return

        while True:
            print("\nEscolha um campo para editar: ")
            # armazena o campo que será editado
            campo_editar = int(
                input(("1- Nome \n 2- Idade \n 3- Email \n 4- Telefone \n 5- Sair: ")))

            if campo_editar == 5:
                break

            # campos do dicionário que podem ser modificados
            campos_dicionario = {1: "nome",
                                 2: "idade", 3: "email", 4: "telefone"}
            # encontra o campo a ser modificado ao mapeá-lo no campos_dicionario
            campo_escolhido = campos_dicionario.get(campo_editar)

            if not campo_escolhido:
                print("Opção inválida")
                continue

            if campo_escolhido == "idade":
                # recebe o novo valor para idade
                novo_valor = input(f"Novo valor para {campo_escolhido}: ")
                if novo_valor.isdigit():  # verificar se o valor de entrada é um número
                    usuario_encontrado[campo_escolhido] = int(novo_valor)
                else:
                    print("Entrada inválida! Campo idade deve ser um número")
                    continue

            novo_valor = input(f"Novo valor para {campo_escolhido}: ")
            usuario_encontrado[campo_escolhido] = novo_valor
            print(f"Campo {campo_escolhido} foi atualizado!")

    except ValueError:
        print("Id não encontrado")


while True:
    print("""\n===== MENU ====
        1 - Cadastrar Usuário
        2 - Listar Usuários
        3 - Atualizar Usuário
        4 - Deletar Usuário
        5 - Sair
""")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção Inválida! Tente novamente")
        continue

    match opcao:
        case 1:
            cadastrarUsuario()
        case 2:
            os.system('cls')
            listarUsuarios()
            time.sleep(2)
        case 3:
            atualizarUsuarios()
        case 5:
            break
