class Profissional:
    def __init__(self, id, nome, email, especialidade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError()
        self.__email = email

    def set_especialidade(self, especialidade):
        if especialidade == "": raise ValueError()
        self.__especialidade = especialidade
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_especialidad(self): return self.__especialidade

    def __str__(self):
        f"id: {self.__id} - nome: {self.__nome} - email: {self.__email} - especialidade: {self.__especialidade}"

    def to_json(self):
            return { "id":self.__id, "nome":self.__nome, "email":self.__email, "especialidade":self.__especialidade}
        
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["email"], dic["especialidade"])