class triangulo:
    def __init__(self):
        self.b = 0  #atributos da classe
        self.h = 0
        #função para calcular a área
    def calc_area(self):
        return self.b * self.h / 2

x = triangulo() #chama o metodo __init__, traz a variavel self para x
print(x.b, x.h)
x.b = float(input("informe a base do triângulo"))
x.h = float(input("informe a altura do triângulo"))
a = x.calc_area() # x ta chamando a função calc_area
print(f"A area do triângulo é {a:.2f}")

y = triangulo() #chama o metodo __init__, traz a variavel self para y
print(y.b, y.h)
y.b = float(input("informe a base segundo do triângulo"))
y.h = float(input("informe a altura do segundo triângulo"))
a = y.calc_area() #nesse caso, quem chama a operação é o y. antes de chamar uma função, deve se especificado quem ta chamando
print(f"A area do segundo triângulo é {a:.2f}")