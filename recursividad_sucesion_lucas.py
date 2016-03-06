#Un ejemplo de sucesión de Fibonacci generalizada es la sucesion de LUCAS
#descrita por la ecuciones
#l0=2
#l1=1
#ln=ln-1 + ln-2 para n=2,3,4......

n=int(input("ingresa el numero N:"))
def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return (lucas(n-1)+lucas(n+1))
print(lucas(n))