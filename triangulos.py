#det si es  equlatero isocele o escaleno
n1 = int(input("lado A:"))
n2 = int(input("lado B:"))
n3 = int(input("lado C:"))

if n1 == n2 == n3:
    print("equilatero")
elif n1==n2 or n2==n3 or n1==n3:
    print ("isocele")
else:
    print ("escaleno")