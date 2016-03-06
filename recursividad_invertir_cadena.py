#funcion recursiva que inviert el orden de una cadena
cad=str(input("ingrese la caden a invertir:"))

def invertit(cad):
    if len(cad)<2:
        return cad
    else:
        return cad[-1]+invertit(cad[:-1])
print(invertit(cad))