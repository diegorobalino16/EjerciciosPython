


n = int(input("esciba el numero:"))

if n>2:
    for i in range (1,n+1):
        for j in range (1,n+1):
            if j==i:
                print("*",end=" ")
            else:
                print("\n")


