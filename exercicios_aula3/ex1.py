class maior:
    def __init__(self, a, b):
        self.valor_a = a
        self.valor_b = b    

    def calc(self):
        if self.valor_a == self.valor_b:
            return "ponha valores diferentes"
        else:
            return max(self.valor_a, self.valor_b)
            

x = maior(int(input()), int(input()))  
print(x.calc()) 