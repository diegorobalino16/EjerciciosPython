#contar numeros pares
#n=int(input("n:"))
#def cuentaPares(n):
#    if (n<10):
#        return 1 - (n % 2)
#    else:
#        m = n // 10
#        return 1 - ((n % 10) % 2) + cuentaPares(m)


#print(cuentaPares(n))


#contar numeros impares
n=int(input("n:"))
def cuentaImpares(n):
    if (n<10):
        return (n % 2)
    else:
        m = n // 10
        return ((n % 10) % 2) + cuentaImpares(m)


print(cuentaImpares(n))