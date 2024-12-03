def cadastrar_contato(id):
    print()
    print('-' * 30 + ' MENU CADASTRAR CONTATOS ' + '-' * 30)
    nome = input('\nDigite o nome do contato: ')
    atividade = input('Digite a atividade que o contato desempenha: ')
    telefone = input('Digite o telefone: ')
    print()

    # Adiciona os valores inseridos pelo usuário em um dicionário
    dados = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    # Insere o dicionário na lista de contatos
    lista_contatos.append(dados)

def consultar_contatos():
    while True:
        print()
        print('-' * 30 + ' MENU CONSULTAR CONTATOS ' + '-' * 30)
        print('\nEscolha a opção desejada: ')
        print('1 - Consultar todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por atividade')
        print('4 - Retornar ao menu')
        escolha = int(input('>> '))

        # Verifica qual foi a escolha do usuário
        match (escolha):
            case 1:
                # Verifica se a lista de contatos está vazia. Caso não esteja, imprime na tela todos os contatos.
                if not lista_contatos:
                    print('A lista de contatos está vazia!')
                else:
                    print('-' * 30)
                    for contato in lista_contatos:
                        for chave, valor in contato.items():
                            print(f'{chave}: {valor}')
                        print('-' * 30)
                    print()
            case 2:
                id = int(input('Digite o Id do contato: '))
                print()
                encontrado = 0
                # Verifica se há algum contato que possui o Id que o usuário inseriu e, em seguida, imprime todos os
                # dados do contato que possui o Id informado.
                for contato in lista_contatos:
                    if contato['id'] == id:
                        encontrado = 1
                        for chave, valor in contato.items():
                            print(f'{chave}: {valor}')
                if not encontrado:
                    print('-' * 30)
                    print('O contato não foi encontrado.')
            case 3:
                atividade = input('Digite a atividade do contato: ')
                print()
                encontrado = 0
                print('-' * 30)
                # Verifica se há algum contato que possui o Id informado pelo usuário e, em seguida, imprime todos os
                # dados do contato.
                for contato in lista_contatos:
                    if contato['atividade'].lower() == atividade.lower():
                        encontrado = 1
                        for chave, valor in contato.items():
                            print(f'{chave}: {valor}')
                        print('-' * 30)
                if not encontrado:
                    print('Nenhum contato foi encontrado.')
            case 4:
                print()
                break
            case _:
                # Esta mensagem aparece quando o usuário escolhe uma opção inválida. Depois disso, o usuário é
                # redirecionado para escolher outra opção.
                print('\nOpção inválida! Tente novamente.')

def remover_contatos():
    print()
    print('-' * 31 + ' MENU REMOVER CONTATOS ' + '-' * 31)
    while True:
        id = int(input('\nDigite o Id do contato (ou digite 0 para sair): '))
        print()

        # Caso o Id for igual a 0, o usuário é redirecionado para o menu principal.
        if id == 0:
            break

        encontrado = 0

        # Procura o contato que possui o Id informado pelo usuário e o apaga.
        for i in range(len(lista_contatos) - 1, -1, -1):
            if lista_contatos[i]['id'] == id:
                encontrado = 1
                del lista_contatos[i]

        # Caso o contato com o Id informado não for encontrado, o usuário é redirecionado para digitar outro Id ou ir
        # para o menu principal. Caso contrário, aparece uma mensagem confirmando que o contato foi removido.
        if not encontrado:
            print('-' * 30)
            print('Id inválido. Tente novamente ou digite 0 para sair.')
        else:
            print('-' * 30)
            print('Contato removido!\n')
            break

# Programa Principal

lista_contatos = []
id_global = 7590435

while True:
    print('-' * 35 + ' MENU PRINCIPAL ' + '-' * 35)
    print('\nEscolha a opção desejada: ')
    print('1 - Cadastrar contato')
    print('2 - Consultar contato')
    print('3 - Remover contato')
    print('4 - Encerrar programa')
    escolha = int(input('>> '))

    match (escolha):
        case 1:
            id_global += 1
            cadastrar_contato(id_global)
        case 2:
            consultar_contatos()
        case 3:
            remover_contatos()
        case 4:
            print('Encerrando programa...')
            break
        case _:
            # Caso o usuário escolher uma opção inválida, aparece esta mensagem e ele é redirecionado para escolher
            # outra opção.
            print('\nOpção inválida! Tente novamente.\n')