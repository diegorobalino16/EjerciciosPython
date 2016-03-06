#escriba una funcion recursiva la cual tome el valor de una cadena y elimine caracters repetidos
#ejemplo:
#recib:HHOLA retorna Hola

cad=str(input("ingrese la cadena:"))
def depurar(cad,cade=""):
    if len(cad)<2:
        return cad+cade
    if cad[-1] in cad[:-1]:
        return depurar(cad[:-1],cade)
    else:
        return depurar(cad[-1],cade+cad[-1])
print(depurar(cad))