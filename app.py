"""Este módulo contém um programa para cadastro de restaurantes.
Ele inclui funcionalidades para cadastrar, listar e ativar restaurantes.
"""


import os
# pylint: disable=missing-function-docstring,

restaurantes = []

def nome_programa():
    print("""
       
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def menu_ops():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar *status* restaurante')
    print('4. Sair\n')


def finalizar():
    ex_subtitulos('finalizando app')

def voltar():
    input('\nDigite uma tecla para voltar ao menu. ')
    main()

def op_invalida():
    print('Opção inválida!\n')
    voltar()

def ex_subtitulos(texto):
    os.system('cls')
    linha ='*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cad_restaurante():
    '''
    Inputs:
    - NOME RESTAURANTE
    - CATEGORIA

    OUTPUT
    - ADICIONA UM NOVO RESTAURANTE PARA LISTA
    

    '''
    ex_subtitulos('Cadastro de novos restaurantes')
    nome_res = input('Digite o nome do restaurante:\n')
    categoria_res = input(f'Digite qual é a categoria do restaurante: {nome_res}: ')
    dados_restaurante = {'nome':nome_res,
    'categoria':categoria_res, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante,{nome_res} foi cadastrado com sucesso!')
    voltar()

def list_restaurante():
    ex_subtitulos('Esses são os restaurantes disponiveis em sistema.')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

      # para cada restaurante na lista restaurantes,
    for restaurante in restaurantes:
        nome_res = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_res.ljust(20)} | {categoria.ljust(20)} | {status}')

    voltar()

def alt_status():
    ex_subtitulos('Alterar status do restaurante')
    nome_res = input('Digite o nome do restaurante que deseja alterar o status: ')
    res_encontrado = False

    for restaurante in restaurantes:
        if nome_res == restaurante['nome']:
            res_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            msg = f'O restaurante {nome_res} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_res} foi desativado com sucesso.'
            print(msg)


    if not res_encontrado:
        print('Restaurante não encontrado')

    voltar()


def exb_opcoes():
    try:
        op_escolhida = int(input('escolha uma opção: '))

        if op_escolhida == 1:
            cad_restaurante()
        elif op_escolhida == 2:
            list_restaurante()
        elif op_escolhida == 3:
            alt_status()
        elif op_escolhida == 4:
            finalizar()
        else:
            op_invalida()
    except ValueError:
        op_invalida()


def main():
    os.system('cls')
    nome_programa()
    menu_ops()
    exb_opcoes()


if __name__ == '__main__':
    main()
