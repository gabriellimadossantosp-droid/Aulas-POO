p = input('digite uma frase')
for i in range(len(p)):
    p = p[1:] + p[0]
    print(p)