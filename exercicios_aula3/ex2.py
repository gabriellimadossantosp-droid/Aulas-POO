class operacao:
    def __init__(self, a, b, str):
        self.valor_a = a
        self.valor_b = b
        self.op_str = str
        self.novo = self.op_str    


    def calc(self):
        if self.op_str == "/":
            return self.valor_a / self.valor_b
        elif self.op_str == "*":
            return self.valor_a * self.valor_b
        elif self.op_str == "+":
            return self.valor_a + self.valor_b
        elif self.op_str == "-":
            return self.valor_a - self.valor_b
        else:
            return "essa operação não é válida"


m = operacao(int(input("valor 1: ")), int(input("valor 2: ")), str(input("digite + ou - ou * ou /: ")))  
print(m.calc())
