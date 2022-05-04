from ast import Return
from salva import mapHashNum
from classe import *


def pesquisaUsuario(Tabela_jogadores, Tabela_usuarios, user_id):
    pos = mapHashNum(user_id, Tam_usuarios)

    if(Tabela_usuarios[pos]):
        for i in range(len(Tabela_usuarios[pos])):
            if(Tabela_usuarios[pos][i].id == user_id):
                ordenaAvals(Tabela_usuarios[pos][i].notas)
                encontraJogadores(Tabela_usuarios[pos][i].notas, Tabela_jogadores)
                return
        print('\nID de usuário não encontrado')
    else:
        print('\nID de usuário não encontrado')


def encontraJogadores(avals, Tabela_jogadores):
    limite = 0

    print("\n{:<15} {:<40} {:<15} {:<15} {:<15}".format('sofifa_id','name','global_rating', 'count', 'rating'))

    while(limite < len(avals) and limite < 20):
        player_id = avals[limite].fifa_id
        player_rating = avals[limite].nota
        pos = mapHashNum(player_id, Tam_jogadores)

        if(Tabela_jogadores[pos]):
            for i in range(len(Tabela_jogadores[pos])):
                if(Tabela_jogadores[pos][i].fifa_id == player_id):
                    name = Tabela_jogadores[pos][i].nome
                    count = Tabela_jogadores[pos][i].num
                    global_ranking = (Tabela_jogadores[pos][i].nota) / count
                    print("{:<15} {:<40} {:<15.6} {:<15} {:<15}".format(player_id, name, global_ranking, count, player_rating))
        limite += 1


def ordenaAvals(avals):
    seq = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711] #ciura
    shellSort(avals, seq)


def shellSort(C, ordem):
    #Procura a posição no vetor dos tamanhos de segmentos
    for j in range(0, len(ordem), 1):
        if ordem[j] >= len(C):
            posicaoOrdem = j-1
            break
    
    #Chama a função de Inserção Direta passando o tamanho do incremento de segmento
    for j in range(posicaoOrdem, -1, -1):
        h = ordem[j]
        insertion_sort(C, h)


def insertion_sort(C, h):
    for i in range(h, len(C)):
        chave = C[i]
        j = i - h

        while(j>=0 and chave.nota > C[j].nota):
            C[j+h] = C[j]
            j -= h
    
        C[j+h] = chave



