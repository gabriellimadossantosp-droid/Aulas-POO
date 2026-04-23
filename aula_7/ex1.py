class retangulo:
    def __init__(self, b, h):
        self.__b = 0
        self.__h = 0
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, v):
        if v >= 0:
            self.__b = v
        else:
            raise ValueError()
        
    def set_altura(self, v):
        if v >= 0:
            self.__h = v
        else:
            raise ValueError
        
    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h
    
    def calc_area(self):
        return self.__b * self.__h / 2
    
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** 0.5
    
    def __str__(self):
        return f"Base = {self.__b} - Altura = {self.__h}" 
    
class frete:
    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)

    def set_distancia(self, v):
        if v > 0:
            self.__d = v
        else:
            raise ValueError("o valor deve ser positivo")
        
    def set_peso(self, v):
        if v > 0:
            self.__p = v
        else:
            raise ValueError("o valor deve ser positivo")
        
    def get_distancia(self):
        return self.__d

    def get_peso(self):
        return self.__p
    
    def calc_frete(self):
        return (0.01 * self.__p) * self.__d

    def __str__(self):
        return f"Peso (kg) = {self.__p} - Distância (km) = {self.__d}"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.retangulo()
            if op == 2: UI.frete()

    @staticmethod
    def menu():
        print("1-Retângulo, 2-Frete, 3-Viagem, 4-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def retangulo():
        print("Cálculo da área do retângulo")
        h = float(input("Informe o valor da base: "))
        b = float(input("Informe o valor da altura: "))
        x = retangulo(h, b)
        area = x.calc_area()
        diagonal = x.calc_diagonal
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area} e diagonal = {diagonal}")

    @staticmethod
    def frete():
        print("Cálculo do valor do frete")
        p = float(input("informe o valor do peso: "))
        d = float(input("informe o valor da distância: ")) 
        x = frete(p, d)
        valor_frete = x.calc_frete()
        print(f"A carga de {x.get_peso()} levada pela distância de {x.get_distancia()} custou {valor_frete} em frete")

UI.main() 