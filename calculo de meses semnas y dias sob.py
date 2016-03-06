n =int(input("ingrese un numero de dias:"))

meses = n//30
semanas =(n%30)//7
dias = (n%30)%7

print ("meses:",meses, "semanas:",semanas, "dias:",dias)
