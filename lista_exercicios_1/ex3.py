lista = []
for i in range(4):
 x = int(input())
 lista.append(x)
 if len(lista) == 4:
     if len(set(lista)) != 4:
        print('erro')
     print(lista[0])
     print(lista[3])
     print(f'a soma resulta em: {lista[1] + lista[2]}')