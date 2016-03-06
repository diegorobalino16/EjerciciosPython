#verifica si un numero esta ordenado de forma ascendente
#


num=int(input("Numero:"))

def ordenar(num):

    if (num<10):
        return 1

    else:
        segundo=num%10
        primero=num%100
        primero=primero//10

        if (primero>segundo):
            return 0
        else:
            return(ordenar(num//10))

print(ordenar(num))