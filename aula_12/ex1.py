from datetime import datetime 

class paciente:
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_id(self, id):
        if id < 0: raise ValueError("ponha esse id direito")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("ponha o nome direito")
        self.__nome = nome

    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("ponha seu cpf mano, qual foi")
        self.__cpf = cpf

    def set_telefone(self, telefone):
        if telefone == "": raise ValueError("irmáozinho coloque esse telefone")
        self.__telefone = telefone

    def set_nascimento(self, nascimento):
        if nascimento > datetime.now(): raise ValueError("você veio do futuro mano?")
        self.__nascimento = nascimento

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento
    
    def __str__(self):
        return f"id: {self.__id} - nome: {self.__nome} - cpf: {self.__cpf} - telefone: {self.__telefone} - nascimento: {self.__nascimento.strftime('%d/%m/%Y')} "
    def idade(self):
        tempo = datetime.now() - self.__nascimento #resulta em um timedelta
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"idade: {anos} ano(s) e {meses} mes(es)"
    
#x = paciente(1, "Eduardo", "001.002.003-45", "84-12345-7890", datetime(2010, 1, 25))
#print(x)
#print(x.idade())

class pacienteUI:
    __pacientes = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = pacienteUI.menu()
            if op == 1: pacienteUI.inserir()
            if op == 2: pacienteUI.listar()
            if op == 3: pacienteUI.atualizar()
            if op == 4: pacienteUI.excluir()
            if op == 5: pacienteUI.pesquisar()
            if op == 6: pacienteUI.aniversariantes()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 9-Fim")
        return int(input("Escolha sua opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        cpf = input("informe o CPF: ")
        telefone = input("informe o telefone: ")
        nascimento = datetime.strptime(input("informe a data de nascimento: "), "%d/%m/%Y")
        x = paciente(id, nome, cpf, telefone, nascimento)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__pacientes: print(x, x.idade())

    @classmethod
    def atualizar(cls):
        id = int(input())
        for x in cls.__pacientes: 
            if x.get_id() == id:
                x.set_nome(input("informe o novo nome:"))
                x.set_cpf(input("informe o novo cpf: "))
                x.set_telefone(input("informe o novo telefone: "))
                x.set_nascimento(datetime.strptime(input("informe a nova data de nascimento: "), "%d/%m/%Y"))

    @classmethod
    def excluir(cls):
        id = int(input("informe o paciente a ser excluído: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.__pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        s = int(input("informe as iniciais do nome"))
        for x in cls.__pacientes:
            if x.get_nome().startswith(s): print(x)

    @classmethod
    def aniversariantes(cls):
        m = int(input("informe o mês para a lista de aniversariantes (1-12): "))
        for x in cls.__pacientes:
            if x.get_nascimento().month == m: print(x)


pacienteUI.main()