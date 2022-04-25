import csv
from salva import *

Tabela_jogadores = [None] * 19739
Tabela_usuarios = [None] * 10007
Tabela_posicoes = [None] * 23
Tabela_tags = [None] * 364961

arquivo = open('Arquivos/players.csv', mode='r')
jogadores = csv.reader(arquivo)
salvaJogadores(Tabela_jogadores, jogadores)
arquivo.close()

arquivo = open('Arquivos/minirating.csv', mode='r')
usuarios = csv.reader(arquivo)
salvaUsuarios(Tabela_jogadores, Tabela_usuarios, usuarios)
arquivo.close()

arquivo = open('Arquivos/players.csv', mode='r')
jogadores = csv.reader(arquivo)
salvaPosicoes(Tabela_posicoes, jogadores)
arquivo.close()







        
