def repetircadena(s,n):
    if n==0:
        return ""
    else:
        return s+repetircadena(s,n-1)

s=input("cadena:")
n=int(input("numero de veces a repetir"))

print(repetircadena(s,n))