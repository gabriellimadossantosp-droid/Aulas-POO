from abc import ABC, abstractclassmethod
class DAO(ABC):
    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._objetos = []
        self._abrir()

    def inserir(self, obj):
        id = 0
        if len(self._objetos) > 0:
            for aux in self._objetos:
                if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self._objetos.append(obj)
        self._salvar()

    def listar(self):
        return self._objetos

    def listar_id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id: return obj
        return None