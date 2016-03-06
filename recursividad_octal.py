
#escriba una funcion recursiva que determine si un numero es octal(es octal cuando la ultima cifra esta entre 0 y7

def esoctal(numero):
    if numero<10:
        if numero<=7 and numero>=0:
            return True
        else:
            return False
    else:
        return esoctal(numero//10)

numero=int(input("numero"))#pedimos el numero

numero=str(numero)#trasformo el numero a cadena

numero=numero[::-1]#invierto el numero

print(esoctal(int(numero)))#ejecuto la funcion recursiva anteriormente implementada