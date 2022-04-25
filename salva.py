from classe import *

tam_jogadores = 19739
tam_usuarios = 10007
tam_posicoes = 23

def salvaJogadores(tabela, jogadores):
    next(jogadores)
    for linha in jogadores:
        id = int(linha[0])
        nome = linha[1]
        posicoes = linha[2].split(', ')
        hashJogador(tabela, id, nome, posicoes)


def salvaUsuarios(tabela_jogadores, tabela_usuarios, usuarios):
    next(usuarios)
    for linha in usuarios:
        user_id = int(linha[0])
        player_id = int(linha[1])
        nota = float(linha[2])
        hashRating(tabela_jogadores, player_id, nota)
        hashUsuario(tabela_usuarios, user_id, player_id, nota)


def hashJogador(tabela, id, nome, posicoes):
    pos = mapHashNum(id, tam_jogadores)
    
    if(tabela[pos]):
        tabela[pos].append(Jogador(id, nome, posicoes))
    else:
        tabela[pos] = []
        tabela[pos].append(Jogador(id, nome, posicoes))


def hashRating(tabela, id, nota):
    pos = mapHashNum(id, tam_jogadores)

    if(tabela[pos]):
        for i in range(len(tabela[pos])):
            if(tabela[pos][i].fifa_id == id):
                tabela[pos][i].nota += nota
                tabela[pos][i].num += 1


def hashUsuario(tabela, user_id, player_id, nota):
    pos = mapHashNum(user_id, tam_usuarios)

    if(tabela[pos]):
        addUsuario(tabela[pos], user_id, player_id, nota)
    else:
        tabela[pos] = []
        addUsuario(tabela[pos], user_id, player_id, nota)


def addUsuario(lista, user_id, player_id, nota):
    if(lista):
        for i in range(len(lista)):
            if(lista[i].id == user_id):
                novaNota(lista[i].notas, player_id, nota)
                return
        criaUsuario(lista, user_id, player_id, nota)
    else:
        criaUsuario(lista, user_id, player_id, nota)
        

def criaUsuario(lista, user_id, player_id, nota):
    novo_usuario = Usuario(user_id)
    novaNota(novo_usuario.notas, player_id, nota)
    lista.append(novo_usuario)


def novaNota(notas, id, nota):
    nova_aval = Notas(id, nota)
    notas.append(nova_aval)


def salvaPosicoes(tabela, jogadores):
    next(jogadores)
    for linha in jogadores:
        id = int(linha[0])
        posicoes = linha[2].split(', ')
        hashPosicoes(tabela, id, posicoes)


def hashPosicoes(tabela, id, posicoes):
    for i in range(len(posicoes)):
        pos = mapHash(posicoes[i], tam_posicoes)
        if(tabela[pos]):
            for j in range(len(tabela[pos])):
                if(tabela[pos][j].posicao == posicoes[i]):
                    if(id not in tabela[pos][j].ids):
                        tabela[pos][j].ids.append(id)
        else:
            nova_posicao = Posicao(posicoes[i])
            nova_posicao.ids.append(id)
            tabela[pos] = []
            tabela[pos].append(nova_posicao)
        


def mapHashNum(id, tam):
    return id % tam


def mapHash(chave, tam):             
    soma = 0
    p = 127
    for i in range(len(chave)):
        soma += ord(chave[i]) * (p**i)
    return soma % tam

