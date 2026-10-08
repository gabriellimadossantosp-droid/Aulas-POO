class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.qtd(qtd)
        self.set_valor(valor)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_id_atendimento(self, id_atendimento):
        if id_atendimento < 0: raise ValueError()
        self.__id_atendimento = id_atendimento

    def set_id_servico(self, id_servico):
        if id_servico < 0: raise ValueError()
        self.__id_servico = id_servico

    def set_qtd(self, qtd):
        if qtd < 0: raise ValueError()
        self.__qtd = qtd

    def set_valor(self, valor):
        if valor < 0: raise ValueError()
        self.__valor = valor

    def __str__(self):
        return f"id: {self.__id} - id atendimento: {self.__id_atendimento} - id serviço: {self.__id_servico} - quantidade: {self.__qtd} - valor: {self.__valor}"

    def to_json(self):
        dic = {"id":self.__id, "id atendimento":self.__id_atendimento, "id serviço":self.__id_servico, "quantidade":self.__qtd, "valor":self.__valor}

    @staticmethod
    def from_json(dic):
        return AtendimentoItens(dic["id"], dic["id_atendimento"], dic["id_servico"], dic["quantidade"], dic["valor"])