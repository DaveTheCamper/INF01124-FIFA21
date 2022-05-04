import csv

class Node:
    def __init__(self, id):
        self.ids = []
        if id != -1:
            self.ids.append(id)
        self.nodes = [None] * 31

    def __getitem__(self, i):
        #print(self.nodes, ' ', i)
        if len(self.nodes) >= i:
            return self.nodes[i]
        else:
            return None

    def __setitem__(self, i, node):
        #print(self.nodes, ' ', i)
        self.nodes[i] = node

    def hasIds(self):
        return len(self.ids) > 0

    def searchJogador(self, prefix):
        next = self
        for c in prefix:
            index = getCharValue(c)
            #print(c, index, next.nodes)
            if next[index]:
                next = next[index]
            else:
                return []

        return next.findAllValues()

    def findAllValues(self):
        list = []
        if self.hasIds():
            list.append(self.ids)

        for n in self.nodes:
            if n is not None:
                for id in n.findAllValues():
                    list.append(id)

        return list

def loadJogadores(tabela_jogadores):
    #next(tabela_jogadores)
    node = Node(-1)
    for linha in tabela_jogadores:
        #print(linha)
        id = linha[0]
        name = linha[1]
        last_node = node
        for c in name:
            index = getCharValue(c)
            #print(c, index)
            if not last_node[index]:
                last_node[index] = Node(-1)
            last_node = last_node[index]
        last_node.ids.append(id)
    return node



def getCharValue(char):
    if char == ' ':
        return 26
    elif char == '-':
        return 27
    elif char == '\'':
        return 28
    elif char == '.':
        return 29
    elif char == '"':
        return 30
    else:
        return ord(char.lower()) - 97


arquivo = open('Arquivos/players.csv', mode='r')
jogadores = csv.reader(arquivo)
#table = [['257261', 'Cameron Antwi', 'CDM']]
mainNode = loadJogadores(jogadores)

print(mainNode.searchJogador("Fernando"))