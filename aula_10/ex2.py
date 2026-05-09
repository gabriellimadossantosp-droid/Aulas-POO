class playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id < 0:
            raise ValueError("o id deve ser positivo")
        self.__id = id
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("tem que escrever algo")
        self.__nome = nome
    
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("tem que escrever algo")
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return "id: {self.__id} - nome: {self.__nome} - descrição: {self.__descricao}"
    
class musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("tem que ser positivo")
        self.__id = id
    
    def set_titulo(self, titulo):
        if titulo == "":
            raise ValueError("põe o titulo da music caramba")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError("não cale o artista")
        self.__artista = artista

    def set_album(self, album):
        if album == "":
            raise ValueError("cadê o album")
        self.__album = album

    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    
    def __str__(self):
        return f"Id = {self.__id} - Titulo = {self.__titulo} - Artista = {self.__artista} - Álbum = {self.__album}"
    
class playlistitem:
    def __init__(self, id, idplaylist, idmusica, sequencia):
        self.set_id(id)
        self.set_idplaylist(idplaylist)
        self.set_idmusica(idmusica)
        self.set_sequencia(sequencia)
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("id deve ser positivo")
        self.__id = id

    def set_idplaylist(self, idplaylist):
        if idplaylist < 0:
            raise ValueError("o id deve ser positivo")
        self.__idplaylist =  idplaylist

    def set_idmusica(self, idmusica):
        if idmusica < 0:
            raise ValueError("o id deve ser positivo")
        self.__idmusica = idmusica

    def set_sequencia(self, sequencia):
        if sequencia < 0:
            raise ValueError("a sequência deve ser positiva")
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id
    def get_idplaylist(self):
        return self.__idplaylist
    def get_idmusica(self):
        return self.__idmusica
    def get_sequencia(self):
        return self.__sequencia
    
    def __str__(self):
        return f"Id = {self.__id} - id da playlist = {self.__idplaylist} - Id da música = {self.__idmusica} - Sequência = {self.__sequencia}"
    
class UI:
    playlist = []
    musica = []
    itens = []
    @staticmethod
    def main():
        op = 0
        while op != 100:
            if op == 1: UI.inserir_palylist()
            if op == 2: UI.inserir_musica()
            if op == 3: UI.inserir_item()
            if op == 4: UI.listar_tudo()