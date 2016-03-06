#Escriba un procedimiento recursivo que modifique una cadena cambiando sus caracteres
#alfabéticos de forma alternada en mayúsculas y minúsculas. En el caso que la cadena contenga
#números o caracteres distintos a letras se los reemplazará por un guión.
#Por ejemplo:
#cadena: 4EspOL56k@ se modifica por: -eSpOl--K
# cadena:exA?meNEs! :) se modifica por: ExA-MeNeS----
#cadena: arco iris se modifica por: ArCo-iRiS

cad=str(input("ingrese la cadena a cambiar:"))
tam=0
y=str
z=str
def cambio(cad):
    x=len(cad)
    y=cad.lower()
    for i in range(0,2):
        z=y[2*i].upper()
        a.apend(z)
    return (a)
print(cambio(cad))

