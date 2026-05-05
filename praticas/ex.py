class vendas:
    def __init__(self, dinheiro):
        self.dinheiro = dinheiro

    def calc(self):
           if self.dinheiro >= 1000:
                print('o vendedor atingiu a meta')
            
           else:
                print('o vendedor não atingiu a meta')

v = vendas(int(input('digite o valor obtido')))
v.calc()