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