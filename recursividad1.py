#Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b. Ejemplos:
#>>> es_potencia(8,2)
#True
#>>> es_potencia(64,4)
#True
#>>> es_potencia(70,10)
#False

n=int(input("ingrese n:"))
b=int(input("ingrese b:"))
def es_potencia(n,b):

    if n//b ==1:
        return True
    else:
        return es_potencia(n//b,b)
        if n//b != 1:
            return es_potencia(n//b,b)
    return False
print(es_potencia(n,b))