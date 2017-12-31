from datetime import datetime
startTime = datetime.now()


def collatz():
    z=3
    ilos = 1
    while z<1000001:
        print (z)
        chain = 0
        x=z
        while x>1:
            if x%2==0:
                x=x/2
            else:
                x=3*x+1
            chain+=1
        if chain>ilos:
            ilos = chain
            naj = z
        z+=1
    return naj


print(collatz())

print(datetime.now() - startTime)