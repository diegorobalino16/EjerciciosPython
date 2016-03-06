from random import *
#matriz de 4x3
a=[]
for i in range(4):
    a=a+[[]]
    for j in range(3):
        a[i]=a[i]+[j]
print(a)

#matriz de 5x3 llena con numeros aleatorios del cero al nueve

b=[]
for f in range(5):
    b=b+[[]]
    for g in range(3):
        b[f]=b[f]+[randint(0,9)]
print(b)