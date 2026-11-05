from models.atendimento import Atendimento
import json

class AtendimentoDAO:
    def __init__(self):
        self._arquivo = "atendimentos.json"
        self._objetos = []
        self.__abrir()

    def inserir(self, obj):
        # gerar um novo id com o maior valor existente mais um
        id = 0
        if len(self._objetos) > 0:
            for aux in self._objetos:
                if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self._objetos.append(obj)
        self.__salvar()

    def listar(self):                
        return self._objetos

    def listar_id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self._objetos.remove(aux)
            self._objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self._objetos.remove(aux)
            self.__salvar()

    def __abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Atendimento.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Atendimento.to_json, indent = 2)
        arquivo.close()
        