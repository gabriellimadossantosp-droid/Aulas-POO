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

class boletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 0:
            op = boletoUI.menu()
            if op == 1: boletoUI.inserir()
            if op == 2: boletoUI.listar()
            if op == 3: boletoUI.atualizar()
            if op == 4: boletoUI.excluir()
            if op == 5: boletoUI.boletos_em_aberto()
            if op == 6: boletoUI.boletos_pagos()
            if op == 7: boletoUI.boletos_a_vencer()
            if op == 8: boletoUI.boletos_vencidos()
            if op == 9: boletoUI.pagar_boletos()

    @staticmethod
    def menu():
        print("---------------------------------------------------")
        print("1 - inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("5 - Boletos em aberto, 6 - Boletos pagos")
        print("7 - Boletos a vencer, 8 - Boletos vencidos")
        print("9 - Pagar boletos, 10 - Fim")
        print("---------------------------------------------------")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        codigo = input("Informe o código do boleto com 10 dígitos: ")
        emissao = datetime.strptime(input("Informe a data de emissão dd/mm/aaaa"), "%d/%m/%Y")
        vencimento = datetime.strptime(input("Informe a data de vencimento dd/mm/aaaa"), "%d/%m/%Y")
        valor = float(input("Informe o valor: "))
        x = boleto(codigo, emissao, vencimento, valor)
        cls.__boletos.append(x)
    
    @classmethod
    def listar(cls):
        for x in cls.__boletos: print(x)

    @classmethod
    def atualizar(cls):
        codigo = input("Informe o código: ")
        for x in cls.__boletos:
            if x.get_cod_barras == codigo:
                x.set_data_emissao(datetime.strptime(input("Informe a nova data de emissão: "), "%d/%m/%Y"))
                x.set_data_vencimento(datetime.strptime(input("Informe a nova data de vencimento: "), "%d/%m/%Y"))
                x.set_valor_boleto(float(input("Informe o novo valor: ")))

    @classmethod
    def excluir(cls):
        codigo = int(input("Informe o código de barras do boleto: "))
        for x in cls.__boletos:
            if x.get_cod_barras() == codigo:
                cls.__boletos.remove(x)

    @classmethod
    def boletos_em_aberto(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == pagamento.EM_ABERTO and x.get_data_vencimento() > datetime.now():
                print(x)

    @classmethod
    def boletos_pagos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == pagamento.PAGO:
                print(x)

    @classmethod
    def boletos_a_vencer(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == pagamento.EM_ABERTO and x.get_data_vencimento() > datetime.now():
                print(x)

    @classmethod
    def boletos_vencidos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == pagamento.EM_ABERTO and x.get_data_vencimento() < datetime.now():
                print(x)

    @classmethod
    def pagar_boletos(cls):
        for x in cls.__boletos:
            codigo = int(input("Informe o código: "))
            for x in cls.__boletos:
                if x.get_cod_barras() == codigo:
                    if x.get_situacao_pagamento() == pagamento.EM_ABERTO:
                        valor = float(input(f"Valor do boleto é R${x.get_valor_boleto():.2f}. Digite o valor pago: "))
                        x.pagar(valor)
                        print("Pagamento efetuado")

boletoUI.main()