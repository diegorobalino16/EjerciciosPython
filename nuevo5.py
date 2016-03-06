#modelo crecimiento poblacional

from math import *

tiempo= int (input("ingrese el tiempo en años a calcular :"))

numero = (5*tiempo + (2*e**(0.1*tiempo)))

print ("el numero de habitatntes sera:", numero)
