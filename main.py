from PesquisaPosicao import pesquisaPosicao
from PesquisaTag import pesquisaTag
from salva import abreArquivos
from PesquisaUsuarios import pesquisaUsuario
from PesquisaPosicao import pesquisaPosicao
from PesquisaNome import pesquisaNome
from classe import *
from menu import *
import time


Tabela_jogadores = [None] * Tam_jogadores
Tabela_usuarios = [None] * Tam_usuarios
Tabela_posicoes = [None] * Tam_posicoes
Tabela_tags = [None] * Tam_tags
tempo_carregamento = [0, 0, 0, 0, 0, 0]
opcao = 0

inicio = time.time()
mainNode = abreArquivos(Tabela_jogadores, Tabela_usuarios, Tabela_posicoes, Tabela_tags, tempo_carregamento)
fim = time.time()
tempo_carregamento[0] = fim - inicio


while opcao != 3:
    tags = []
    opcao = menu()

    if(opcao == 1):
        imprimeFormatos()
        entrada = input('\n$ ').lower().split(' ', 1)
        
        if(entrada[0] == 'user'):
            if isinstance(entrada[1], int):
                user_id = int(entrada[1])
                pesquisaUsuario(Tabela_jogadores, Tabela_usuarios, user_id)
            else:
                print('O ID do usuário deve ser um numero')
        
        elif(entrada[0] == 'tags'):
            tags = entrada[1].split("'")[1::2]
            print(tags)
            pesquisaTag(Tabela_jogadores, Tabela_tags, tags)
        
        elif(entrada[0][0] == 't' and entrada[0][1] == 'o' and entrada[0][2] == 'p'):
            tam = entrada[0].split('p')
            tam = int(tam[1])
            posicao = entrada[1].strip()[1:-1].lower()
            pesquisaPosicao(Tabela_jogadores, Tabela_posicoes, posicao, tam)

        elif(entrada[0] == 'player'):
            prefixo = entrada[1].lower()
            pesquisaNome(Tabela_jogadores, mainNode, prefixo)


        else:
            print('\nPor favor, digite a sua entrada de acordo com os formatos de pesquisa\n')

    elif(opcao == 2):
        print(f'\nTempo carregamento jogadores: {tempo_carregamento[1]}')
        print(f'Tempo carregamento usuários: {tempo_carregamento[2]}')
        print(f'Tempo carregamento posições: {tempo_carregamento[3]}')
        print(f'Tempo carregamento tags: {tempo_carregamento[4]}')
        print(f'Tempo carregamento nomes: {tempo_carregamento[5]}')
        print(f'Tempo total de carregamentos: {tempo_carregamento[0]}')
    
    else:
        print('\nPrograma encerrado')
    
    








        
