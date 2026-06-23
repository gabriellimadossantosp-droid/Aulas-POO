x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
x["AM"] = "Manaus"
# x[5] = "teste"
# y = {"PB"} = "J. Pessoa"
print(x)
print(*x)
print(len(x))
print(max(x))

for item in x.items(): print(item)
for item in x: print(item)