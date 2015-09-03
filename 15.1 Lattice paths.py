from datetime import datetime
startTime = datetime.now()

def taxi(n):
    kol1 = []
    for x in range(1,n+1):
        kol1.append(1)
    kol2 = []
    suma=0
    for x in range(1,n+1):
        suma+=kol1[x-1]
        kol2.append(suma)
    kol3=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol2[x-1]
        kol3.append(suma)
    kol4=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol3[x-1]
        kol4.append(suma)
    kol5=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol4[x-1]
        kol5.append(suma)
    kol6=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol5[x-1]
        kol6.append(suma)
    kol7=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol6[x-1]
        kol7.append(suma)
    kol8=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol7[x-1]
        kol8.append(suma)
    kol9=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol8[x-1]
        kol9.append(suma)
    kol10=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol9[x-1]
        kol10.append(suma)
    kol11=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol10[x-1]
        kol11.append(suma)
    kol12=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol11[x-1]
        kol12.append(suma)
    kol13=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol12[x-1]
        kol13.append(suma)
    kol14=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol13[x-1]
        kol14.append(suma)
    kol15=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol14[x-1]
        kol15.append(suma)
    kol16=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol15[x-1]
        kol16.append(suma)
    kol17=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol16[x-1]
        kol17.append(suma)
    kol18=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol17[x-1]
        kol18.append(suma)
    kol19=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol18[x-1]
        kol19.append(suma)
    kol20=[]
    suma=0
    for x in range(1,n+1):
        suma+=kol19[x-1]
        kol20.append(suma)
    wynik = 2*(kol1[-1]+kol2[-1]+kol3[-1]+kol4[-1]+kol5[-1]+kol6[-1]+kol7[-1]+kol8[-1]+kol9[-1]+kol10[-1]+kol11[-1]+kol12[-1]+kol13[-1]+kol14[-1]+kol15[-1]+kol16[-1]+kol17[-1]+kol18[-1]+kol19[-1]+kol20[-1])
    return wynik
print(taxi(20))
print(datetime.now() - startTime)