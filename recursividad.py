#cuenta los numero de un numero

n=int(input("ingrese el  numero n:"))

def numeros (n):
    if n<10:
        return 1
    else:
        return numeros(n//10)+1

print(numeros(n))