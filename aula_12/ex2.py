from enum import Enum
from datetime import datetime

class pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class boleto:
    def __init__(self, codigo, emissao, vencimento, valor):
        #Esses atributos serão validados
        self.set_cod_barras(codigo)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(vencimento)
        self.set_valor(valor)
        #Atributos com valor inicial pré-definido
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = pagamento.EM_ABERTO

    def set_cod_barras(self, codigo):
        #supondo que esse código deve ter 10 dígitos
        if len(codigo) != 10: raise ValueError("o código deve ter 10 dígitos")
        self.__cod_barras = codigo

    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("Você não pode emitir uma conta do futuro")
        self.__data_emissao = emissao

    def set_data_vencimento(self, vencimento):
        if vencimento < datetime.now(): raise ValueError("Não tem como esse boleto ter vencido no passado se tá saindo agora")
        self.__data_vencimento = vencimento

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Impossível ter dívida negativa")
        self.__valor = valor

    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError("Não tem como pagar com dinheiro negativo")
        if  self.__situacao_pagamento != pagamento.EM_ABERTO: raise ValueError("Calma chefe, tu já pagou")
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_boleto == self.__valor_pago: self.__situacao_pagamento = pagamento.PAGO
        else: self.__situacao_pagamento = pagamento.PAGO_PARCIAL

    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_valor_boleto(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_pago
    def get_data_pagamento(self): return self.__data_pagamento
    def get_situacao_pagamento(self): return self.__situacao_pagamento

    def __str__(self):
        s = f"Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime("%d/%m/%Y")}"
        s += f"Valor: RS {self.__valor_boleto:.2f} - Valor Pago: RS {self.__valor_pago:.2f}"
        s += f"Vencimento: {self.__data_emissao.strftime("%d/%m/%Y")}"
        s += f"Data de Pagamento: {self.__data_pagamento}"
        s += f"Situação: {self.__situacao_pagamento}"
        return s
