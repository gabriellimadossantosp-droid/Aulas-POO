a = int(input())
b = int(input())
c = int(input())
d = int(input())
soma_pares = 0
soma_impares = 0

if a % 2 == 0:
    soma_pares += a
else:
    soma_impares += a

if b % 2 == 0:
    soma_pares += b
else:
    soma_impares += b

if c % 2 == 0:
    soma_pares += c
else:
    soma_impares += c
    
if d % 2 == 0:
    soma_pares += d
else:
    soma_impares += d

print(soma_pares, soma_impares)