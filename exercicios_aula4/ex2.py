class Pais:
        def __init__(self, nome, populacao, area):
                self.nome = nome
                        self.populacao = populacao
                                self.area = area

                                    def calcular_densidade(self):
                                            return self.populacao / self.area

                                            paises = []

                                            for i in range(1, 11):
                                                nome = input("Digite o país: ")
                                                    populacao = int(input("Digite a população: "))
                                                        area = float(input("Digite a área: "))
                                                            
                                                                pais_novo = Pais(nome, populacao, area)
                                                                    paises += [pais_novo]

                                                                    densidade_grande = paises[0]

                                                                    for pais in paises:
                                                                        if pais.calcular_densidade() > densidade_grande.calcular_densidade():
                                                                                densidade_grande = pais

                                                                                print(f"{densidade_grande.nome} tem a densidade de {densidade_grande.calcular_densidade()}")

