def fib(x):
    f1=0
    f2=1
    il = 0
    while 1<2:
        f1+=f2
        f2+=f1
        if len(list(str(f1))) == x or len(list(str(f2))) == x:
            if len(list(str(f1))) > len(list(str(f2))):
                return il+1
            else:
                return il+2
        il+=2
print(fib(1000))