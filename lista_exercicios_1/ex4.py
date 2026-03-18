print("digite uma data no formato dd/mm/aaaa")
data =int(input())
mes = input()
ano = int(input())

data_invalida = False 

if not(1900 <= ano <= 2100):
    data_invalida = True
if not(1 <= mes <= 12):
    data_invalida = True 