class Jogador:
    def __init__(self, fifa_id, nome, posicao):
        self.fifa_id = fifa_id
        self.nome = nome
        self.posicao = posicao
        self.nota = 0
        self.num = 0


class Usuario:
    def __init__(self, id):
        self.id = id
        self.notas = []


class Notas:
    def __init__(self, fifa_id, nota):
        self.fifa_id = fifa_id
        self.nota = nota

class Posicao:
    def __init__(self, posicao):
        self.posicao = posicao
        self.ids = []

