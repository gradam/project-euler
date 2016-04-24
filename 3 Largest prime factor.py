def bprime(kupa):
    pier = []
    for x in range(2,kupa):
        while kupa%x==0:
            pier.append(x)
            kupa=kupa/x
            print(pier)
    pier.sort()
    wyn = pier[-1]
    return(wyn)
print(bprime(13195))
