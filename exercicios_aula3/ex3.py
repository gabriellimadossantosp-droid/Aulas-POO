def soma(frase):
    soma = 0
    for i in frase:
        if i.isdigit():
            soma += int(i)
    return soma


print(soma(input("Digite uma frase: ")))
