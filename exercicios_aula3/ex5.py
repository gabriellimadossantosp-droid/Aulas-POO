class dados_pais:
    def __init__(self, nome, populacao, km):
        self.nome = nome
        self.populacao = populacao
        self.km = km

    def calculo(self):
        densidade = self.populacao / self.km
        print(f"densidade demográfica do {self.nome} é de {densidade:.2f} hab/km2")
        
x = dados_pais(str(input("digite o nome do país: ")), int(input("digite o a população do país: ")), int(input("digite a área em km ao quadrado do país: ")))
x.calculo()