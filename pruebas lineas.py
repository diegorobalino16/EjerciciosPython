
correos=open("archivo.txt","r+")
dicc=()

for lineas in correos:
    separa=lineas.split("@")
    clave=separa[1][:1]
    if clave in dicc:
        cont=cont+1
    else:
        dicc
    print(clave)
    print(dicc)
