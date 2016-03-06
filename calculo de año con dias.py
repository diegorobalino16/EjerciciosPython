
n =int(input("ingrese un numero de dias:"))

#años= n//365
#meses = (n%365)//30
#dias = (n%365)%30
#print ("dias:", dias ,"meses:", meses,"años:",años)

[a,dm] = divmod(n,365)
[m,d] = divmod (dm,30)
print ("dias:", d ,"meses:", m,"años:",a)