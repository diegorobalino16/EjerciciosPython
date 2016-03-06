kw =int(input("ingrese los kw:"))
pkw = int(input("ingrese un numero de dias:"))

if kw > 700:
    ex = kw - 700
    pagar = (kw*pkw)+(ex*0.05)
    print (pagar)
else:
    pago=(kw*pkw)
    print (pago)

