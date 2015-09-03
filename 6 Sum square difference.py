def roz(x):
    b=0
    c=0
    lcz = []
    for a in range(1,(x+1)):
        b+=a**2
        c+=a
    z=c**2-b
    return z
print(roz(100))