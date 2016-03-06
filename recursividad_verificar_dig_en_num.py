#Escriba la función int frecuencia (int numero, int digito); la cual retorna
#el número de veces que
#digito se encuentra en numero.
#Por ejemplo:
#numero: 1218 y digito : 1, retorna 2
#numero: 678 y digito : 9 , retorna 0

def frecuencia (num,dig):
    while num < 10:
        if num==dig:
            return 1
        else:
            return 0

    if num%10 == dig:
        return frecuencia(num//10,dig)+1
    else:
        return frecuencia(num//10,dig)

num=int(input("ingrese el numero:"))
dig=int(input("ingrese el digito:"))
print(frecuencia(num,dig))

