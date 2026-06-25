from datetime import datetime
import json

class contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_id(self, id):
        if id < 0: raise ValueError("o id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("ponha seu nome")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("ponha seu email")
        self.__email = email

    def set_telefone(self, telefone):
        if telefone == "": raise ValueError("ponha seu telefone")
        self.__telefone = telefone

    def set_nascimento(self, nascimento):
        if nascimento > datetime.now(): raise ValueError("não tem como nascer no futuro")
        self.__nascimento = nascimento

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        f"id:: {self.__id} - Nome: {self.__nome} - Email: {self.__email} - Telefone: {self.__telefone} - Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"


class contatoUI:
    __contatos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = contatoUI.menu()
            if op == 1: contatoUI.inserir()
            if op == 2: contatoUI.listar()
            if op == 3: contatoUI.listar_id()
            if op == 4: contatoUI.atualizar()
            if op == 5: contatoUI.excluir()
            if op == 6: contatoUI.pesquisar()
            if op == 7: contatoUI.aniversariantes()
            if op == 8: contatoUI.abrir()
            if op == 9: contatoUI.salvar()

    @staticmethod
    def main():
        print("1 - Inserir, 2 - Listar, 3 - Listar id")
        print("4 - Atualizar, 5 -Excluir, 6 - Pesquisar ")
        print("7 - Aniversariantes, 8 - Abrir, 9 - Salvar")
        print("10 - Fim")
        return int(input("Escolha uma opção: "))

    