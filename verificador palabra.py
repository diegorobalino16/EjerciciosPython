#verifica si los caracteres de la pabra estan ordenados alfabeticamente


palabra=input("PALABRA:")

def ordenado(palabra):
    if (len(palabra)<2):
        return 1
    else:
        primero=ord(palabra[0])
        segundo=ord(palabra[1])
        if segundo < primero:
            return 0
        else:
            return(ordenado(palabra[1:]))


print(ordenado(palabra))