n=int(input("ingresa n:"))
a=[]




def orden(n):
    if n<10:
        return 0
    else:
        num=n%10
        a.append(num)
        print(a)
        return orden(n//10)
    for i in a:
        if a[i] <= a[i+1]:
            return 1
        else:
            return 0





print(orden(n))