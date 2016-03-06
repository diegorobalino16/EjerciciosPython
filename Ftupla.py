A=(1,2,3,4)
B=(3,4,5,6,7,8)

def tupla (A,B):
    X=set(A)
    Y=set(B)
    m=X^Y
    G=tuple(m)
    return G
print(tupla(A,B))