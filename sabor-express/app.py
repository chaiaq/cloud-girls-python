import os

# restaurantes = ['Pizza', 'Sushi', 'Lasanha']

# uso de dicionários:
restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False},
                {'nome':'Biscoito', 'categoria':'massas', 'ativo':True},
                {'nome':'Yoki', 'categoria':'pizza', 'ativo':False}]

def exibir_nome_programa():

    print("""
▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ ▀▄▒▄▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀▀█ 
░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ░▒█░░ ▒█▄▄█ ▒█▄▄▀ ▒█▀▀▀ ░▀▀▀▄▄ ░▀▀▀▄▄ 
▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▄▀▒▀▄ ▒█░░░ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▒█▄▄▄█
      
      """)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    # para cada caractere no texto imprimir um asterisco:
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def retorne():
    input('\nDigite uma tecla para retornar ao menu principal')    
    main()

def finalizar_app():
        exibir_subtitulo('Finalizando o programa')

def opcao_invalida():
    print('Opção inválida!\n')
    retorne()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes:')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,
                            'categoria':categoria_do_restaurante,
                            'ativo':False}
    # todo restaurante inicia desativado
    restaurantes.append(dados_do_restaurante)
    print(f'{nome_do_restaurante} cadastrado com sucesso!')
    retorne()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes:')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativacao = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativacao}')
        # função ljust ajusta a extensão do conteúdo
    retorne()

def alternar_restaurante():
    exibir_subtitulo('Alternando estado do restaurante:')
    nome_restaurante = input('Digite o nome do restaurante para alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado') 


    retorne()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}!')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()