from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
            self.set_nome(nome)
            self.set_cpf(cpf)
            self.set_telefone(telefone)
            self.set_nascimento(nascimento)

    def set_nome(self, nome):
            if nome == "": raise ValueError()
            self.__nome = nome
    def set_cpf(self, cpf):
            if cpf == "": raise ValueError()
            self.__cpf = cpf
    def set_telefone(self, telefone):
            if telefone == "": raise ValueError()
            self.__telefone = telefone
    def set_nascimento(self, nascimento):
            if nascimento > datetime.now(): raise ValueError()
            self.__nascimento = nascimento

    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime('%d/%m/%Y')}"

    def idade(self):
        x = datetime.now() - self.__nascimento #idade
        dias = x.days  #dias vividos
        meses = dias % 365 // 30
        anos = dias // 365      
        return f"{anos} anos e {meses} mes(es)"                 

