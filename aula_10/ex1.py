class time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Põe um nome aí seu bocó")
        self.__nome = nome 

    def set_estado(self, estado):
        if estado == "":
            raise ValueError("Põe o nome do estado aí seu bobão")
        self.__estado = estado

    def set_id(self, id):
        if id < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__id = id

    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"time {self.__nome} - estado {self.__estado} - id {self.__id}"
    
class jogador:
    def __init__(self, id, nome, idtime, camisa):
        self.set_id(id)
        self.set_nome(nome)
        self.set_idtime(idtime)
        self.set_camisa(camisa)
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Põe um nome aí seu bocó")
        self.__nome = nome 
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__id = id

    def set_idTime(self, idtime):
        if idtime < 0:
            raise ValueError("O seu id deve ser positivo")
        self.__idtime = idtime
    
    def set_camisa(self, camisa):
        if camisa < 0:
            raise ValueError("tem que ser maior que zero papai")
        self.__camisa = camisa
    
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    def get_idtime(self):
        return self.__idtime
    def get_camisa(self):
        return self.__camisa
    
    def __str__(self):
        return f"nome do jogador: {self.__nome} - id do jogador: {self.__id} - idTime: {self.__idtime} - camisa: {self.__camisa}"