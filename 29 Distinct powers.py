def gen(amin,amax,bmin,bmax):
    lst=[]
    for a in range(amin, amax+1):
        for b in range(bmin, bmax+1):
            lst.append(a**b)
    return len(list(set(lst)))
print(gen(2,100,2,100))