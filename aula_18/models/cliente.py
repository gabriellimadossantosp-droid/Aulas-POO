class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(fone)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}"
    def set_id(self, id):
        if id < 0: raise ValueError("o id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("tem que colocar um nome")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("tem que colocar um email")
        self.__email = email

    def set_telefone(self, fone):
        if fone == "": raise ValueError("tem que colocar um telefone")
        self.__telefone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_telefone(self): return self.__telefone

    def to_json(self):
        return {"id" : self.__id, "nome" : self.__nome, "email" : self.__email, "telefone" : self.__telefone}

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"])