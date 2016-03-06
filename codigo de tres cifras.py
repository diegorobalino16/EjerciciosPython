
cod = input("engrese el codigo de tres numero:")
x = len(cod)
if x <= 3:

    y = int(cod[0])*int(cod[1])
    z=y%10
    if z==int(cod[2]):
        print ("esta codificado")
    else:
        print ("no esta codificado")
else:
    print ("el num ingresado no es valido")
