from usuario import Usuario
# from conexao import Conexao

# MENU que contém as opções das funções (metódos) criadas nos demais arquivos deste projeto
def menu():
    while True:
        op = int(input('==== SISTEMA DE USUÁRIOS ==== \n1- Cadastrar usuário \n2- Listar usuários \n3- Atualizar usuário \n4- Excluir usuário \n5- Sair \nInsira uma opção: '))
        match op:
            case 1:
                print('==== CADASTRO DE USUÁRIO ====')
                nome = input('Nome: ')
                email = input('Email: ')
                idade = input('Idade: ')

                usuario1 = Usuario(nome,email,idade)

                usuario1.salvar()
            case 2:
                Usuario.listar()
            case 3:
                print('==== ATUALIZAÇÃO | CADASTRO DE USUÁRIO ====')

                atualizarcoisa = int(input('Insira o ID a ser ATUALIZADO: '))
                                     
                nome = input('Nome: ')
                email = input('Email: ')
                idade = input('Idade: ')

                usuario1 = Usuario(nome,email,idade)
                usuario1.atualizar(atualizarcoisa)
            case 4:
                removercoisa = int(input('Insira o ID a ser REMOVIDO: '))
                Usuario.excluir(removercoisa)
            case 5:
                print('Saindo...')
                break
            case __: # Caso o usuário digite uma opção diferente das citadas no menu
                print('Opção inválida...')
                return 

menu() ##Executa o menu quando é iniciado