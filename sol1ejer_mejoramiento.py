from random import *

n=int(input("numero de elementos de la lista:"))
lista=[]
for i in range(n):
    numero=randrange(0,101)
    lista.append(numero)
print(lista)
clista=set(lista)
lista=list(clista)
lista.sort()
print(lista[1])
