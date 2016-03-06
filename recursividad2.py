#de digitos de un numero

n=int(input("n:"))

def num(n):
    if n<10:
        return 1
    else:
        return num(n//10)+1

print(num(n))