#Escriba una función recursiva que calcule el máximo común divisor de dos números (mcd). El mcd
#de dos números es el número más grande para el que se pueden dividir ambos teniendo residuo 0.
#Para encontrar el máximo común divisor de dos números naturales a y b, se siguen las siguientes
#reglas:
#• Si b=0 entonces mcd(a,b)=a.
#• En otros casos, mcd(a,b)=mcd(b,r) donde r es el residuo de dividir a entre b.
#Para calcular mcd(b,r) se utilizan estas mismas reglas.
#Por ejemplo:
#Divisores de 60 son 1,2,3,4,5,6,10,12,15,20,30,60
#Divisores de 48 son 1,2,3,4,6,8,12,16,24,48
#El máximo común divisor de ambos es 12.

def maximo_divisor(a,b):
    if b==0:
        return a
    else:
        return maximo_divisor(b,a%b)
a=int(input("ingrese el numero:"))
b=int(input("ingreseotro numero:"))

print(maximo_divisor(a,b))