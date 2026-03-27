def soma(numeros):
    soma = 0
    for i in numeros:
        if i.isdigit():
            soma += int(i)
    return soma

print(soma(input("coloque uma lista de números: ")))