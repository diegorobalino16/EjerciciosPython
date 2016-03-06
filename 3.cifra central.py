#dos numeros de 3 cifras , sume las cifras centrales

x =int(input("ingrese un numero entero de 3 cifras:"))
y =int(input("ingrese un numero entero de 3 cifras:"))


mx = (x//10)%10 #para x
my = (y//10)%10 #para y

print("la suma de los numeros intermedio es :",mx + my)
