class viagem:
    def __init__(self, des, dis, l):
        self.__des = ''
        self.__dis = 0
        self.__l = 0
        self.set_destino(des)
        self.set_distancia(dis)
        self.set_litros(l)

    def set_destino(self, v):
       if v != '':
          self.__des = v
       else:
          raise ValueError 

    def set_distancia(self, v):
        if v >= 0:
          self.__dis = v
        else:
          raise ValueError
        
    def set_litros(self, v):
       if v >= 0:
          self.__l = v
       else:
          raise ValueError
       
    def get_destino(self):
       return self.__des
    
    def get_distancia(self):
       return self.__dis
    
    def get_litros(self):
       return self.__l
    
    def calc_consumo(self):
       return self.__dis / self.__l
       
    def __str__(self):
        return f"Destino = {self.__des} - distância = {self.dis} - gasto em litros = {self.l}"
    
class Pais:
    def __init__(self, n: str, p: int, a: float):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, v):
        if v != '':
            self.__nome = v
        else:
            raise ValueError("Nome inválido")

    def set_populacao(self, v):
        if v >= 0:
            self.__populacao = v
        else:
            raise ValueError("População inválida")

    def set_area(self, v):
        if v > 0:
            self.__area = v
        else:
            raise ValueError("Área deve ser maior que zero")

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def densidade(self):
        return self.__populacao / self.__area

    def __str__(self):
        return f"Nome: {self.__nome}, População: {self.__populacao}, Área: {self.__area} km²"

class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.viagem()
            if op == 2: ViagemUI.Pais()

    @staticmethod
    def menu():
        print("1-Viagem, 2-Pais, 4-Fim")
        op = int(input("Informe uma opção: "))
        return op    
    
    @staticmethod
    def viagem():
       destino = str(input("informe o destino"))
       distancia = float(input("informe a ditancia"))
       litros =  float(input("informe os litros"))
       x = viagem(destino, distancia, litros)
       consumo = x.calc_consumo
       print(f"a viagem com destino a {x.get_destino()}, de distância {x.get_distancia()} teve o custo médio de {consumo}")

    @staticmethod
    def calculo_p():
        nom = input("Nome do país: ")
        popu = int(input("População: "))
        are = float(input("Área (km²): "))

        x = Pais(nom, popu, are)
        print(x)
        print(f"Densidade demográfica: {x.densidade():.2f} hab/km²")


ViagemUI.main()



