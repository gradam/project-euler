def bprime(liczba):
    pier = []
    for x in range(2,liczba):
        while liczba%x==0:
            pier.append(x)
            liczba=liczba/x
            print(pier)
        if liczba == 1:
            break
    pier.sort()
    wyn = pier[-1]
    return(wyn)
print(bprime(13195))
