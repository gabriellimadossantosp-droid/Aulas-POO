class agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
    
    def calc(self):
        preco = 0
        if self.consumo <= 10:
            preco = 38
        
        elif 11 <= self.consumo <= 20:
            preco = 38 + (self.consumo - 10) * 5
        
        elif self.consumo >= 21:
            preco = 88 + (self.consumo - 20) * 6

        print(preco)

x = agua(str(input("digite o mes: ")),float(input("digite o ano: ")), float(input("digite o consumo: ")))
x.calc()