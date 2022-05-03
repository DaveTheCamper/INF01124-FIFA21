from PesquisaPosicao import pesquisaPosicao
from salva import abreArquivos
from PesquisaUsuarios import pesquisaUsuario
from PesquisaPosicao import pesquisaPosicao
from classe import *
from menu import menu

Tabela_jogadores = [None] * Tam_jogadores
Tabela_usuarios = [None] * Tam_usuarios
Tabela_posicoes = [None] * Tam_posicoes
Tabela_tags = [None] * Tam_tags
opcao = 0

abreArquivos(Tabela_jogadores, Tabela_usuarios, Tabela_posicoes, Tabela_tags)
while opcao != 3:
    opcao = menu()

    if(opcao == 1):
        pesquisaUsuario(Tabela_jogadores, Tabela_usuarios)
    
    elif(opcao == 2):
        pesquisaPosicao(Tabela_jogadores, Tabela_posicoes)
    
    elif(opcao == 3):
        print('Programa encerrado')
    
    else:
        print('Opcão inválida. Digite novamente')

#for i in Tabela_posicoes:
 #   print(i)







        
