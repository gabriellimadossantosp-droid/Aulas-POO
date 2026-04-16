class retangulo:
    def __init__(self):
        self.__base = 0   #os dois traços ao lado dos atributos deixa eles encapsulados (ocultos)
        self.__altura = 0 

    def set_base(self, valor): #ao chamarmos a função que define o valor, devemos usar a função set
        if valor < 0:
            raise ValueError("o valor deve ser positivo")
        self.__base = valor 
    def get_base(self):        #função get serve para pegar o valor setado
        return self.__base
    
    def set_altura(self, valor):
        if valor < 0:
            raise ValueError("o valor deve ser positivo")
        self.__altura = valor
    def get_altura(self):
        return self.__altura 
    
    def diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5
class UI:
    def main():
        x = retangulo()
        x.set_base(float(input()))
        x.set_altura(float(input()))
        print(f"o retangulo de base {x.get_base()} e altura {x.get_altura()}")
        diagonal = x.diagonal
        print(diagonal)

UI.main()