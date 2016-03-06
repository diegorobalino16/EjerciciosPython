lista = [2, 4, 8, 5, 5, 3]
x = lista[0] # x vale el primer valor de la lista

for i in lista:
    if i < x:
        x = i

print (x)
