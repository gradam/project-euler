import math
import time

startTime = time.time()

def triangle():
    z = 1
    x = 0
    while True:
        lst=[]
        x+=z
        for a in range(1,round(math.sqrt(x))):
            if x % a == 0:
                lst.append(a)
            if len(lst)>=250:
                lst2=[]
                for m in lst:
                    lst2.append(m)
                    lst2.append(x/m)
                lst2.sort()
                return lst2
        z += 1
print(triangle())
print(time.time()-startTime)