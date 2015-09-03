def szukacz():
    a=100
    b=100
    z=1
    lst = []
    while a<1000:
        while b<1000:
            num=a*b
            num2 = str(num)
            lst3 = []
            for x in num2:
                lst3.append(x)
            lst4=[]
            for x in reversed(lst3):
                lst4.append(x)
            if lst4 == lst3:
                num4 = "".join(lst4)
                num4 = int(num4)
                lst.append(num4)
            b+=1
        a+=1
        b=100+z
        z+=1
    lst.sort()
    wynik = lst[-1]
    return wynik

print(szukacz())