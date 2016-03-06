import numpy
cas=0#cuenta los casilleros cambiados por ceros


tablero=numpy.random.random_integers(1,4,(10,10))#me genera el tablero


def isInside(i,j):
    return (i >= 0 and i <10) and (j >= 0 and j < 10)


def veri_amigos(i,j,valor):
    if (not isInside(i,j)) or valor==tablero[i+1][j] or valor==tablero[i-1][j] or valor==tablero[i][j+1] or valor==tablero[i][j-1]:
         eliminar_casilla(i,j,valor)
    else:
        return tablero



def eliminar_casilla(i,j,valor): #funcion recursiva que me permite ubicar los casilleros amigos a eliminar
    global cas
    if tablero[i][j] != valor:
        return
    tablero[i][j] = 0
    cas+= 1

    eliminar_casilla(i+1,j,valor)
    eliminar_casilla(i-1,j,valor)
    eliminar_casilla(i,j+1,valor)
    eliminar_casilla(i,j-1,valor)

def imprimir_tablero():
    for i in range(0,10):
        if (i+1) < 10:
            print(str(i+1)+"  | "+str(tablero[i]))
        else:
            print(str(i+1)+" | "+str(tablero[i]))

    print("   ",end="")
    for i in range(0,23):
        print("-",end="")
    print(" ")
    print("      ",end="")
    for i in range(0,10):
        print(str(i+1),end=" ")
    print(" ",end="\n\n")

imprimir_tablero()
print("__________________________")

num_fila=int(input("ingrese el numero de la fila:"))
num_col=int(input("ingrese el numero de la columna:"))


veri_amigos(num_fila-1,num_col-1,tablero[num_fila-1][num_col-1])



imprimir_tablero()
print(cas)



