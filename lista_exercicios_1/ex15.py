print("digite um número inteiro")
n = int(input())
primo = True

for d in range(2, n): #basta ir até a raiz quadrada
    if n % d == 0:
        primo = False
    if primo == False: #if not primo
        break
if primo: #if primo 
    print(n, 'é primo')
else:
    print(n, 'não é primo')