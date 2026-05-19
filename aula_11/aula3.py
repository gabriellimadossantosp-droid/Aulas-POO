from datetime import datetime
#o primeiro datetipe é um módulo

x = int(input("informe um número inteiro: "))
print(x)

d = datetime.strptime(input('informe uma data: '), '%d/%m/%Y')
#o segundo datetipe é uma classe
print(d)
print(d.strftime("%d/%m%Y"))

#strptime - passa de string para datetime. é um método estático, chama com uma classe
#strftime - passa de datetime para string. método de instância, chama com uma variável de classe (objeto)