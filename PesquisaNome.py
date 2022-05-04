from classe import Tam_jogadores
from trie import *
from salva import mapHashNum
from PesquisaPosicao import ordenaPosicoes

def pesquisaNome(Tabela_jogadores, trie, prefixo):
    ids = trie.searchJogador(prefixo) #Extrai os ids com o prefixo da árvore trie
    
    if(ids): #Caso encontre os ids do prefixo
        for i in range(len(ids)):
            ids[i] = int(ids[i])
        encontraJogadores(ids, Tabela_jogadores)
    else:
        print('\nNenhum jogador encontrado')
        return


def encontraJogadores(ids, Tabela_jogadores):
    ordenaPosicoes(ids, Tabela_jogadores)

    print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format('sofifa_id','name','player_positions', 'rating', 'count'))
    
    #Imprime cada jogador de cada id extraido da árvore trie
    for i in range(len(ids)):
        pos = mapHashNum(ids[i], Tam_jogadores)

        for j in range(len(Tabela_jogadores[pos])):
            if(Tabela_jogadores[pos][j].fifa_id == ids[i]): #Ao encontrar o id do jogador na tabela Hash de jogadores, imprime suas informações
                if(Tabela_jogadores[pos][j].num != 0):
                    rating = Tabela_jogadores[pos][j].nota / Tabela_jogadores[pos][j].num
                else:
                    rating = 0.0
                print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format(Tabela_jogadores[pos][j].fifa_id, Tabela_jogadores[pos][j].nome, ', '.join(Tabela_jogadores[pos][j].posicao), rating, Tabela_jogadores[pos][j].num))

