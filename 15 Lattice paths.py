def grid(x):
    il = 0; kol1 = []; kol2=[]; kol3=[]; kol4=[]; kol5=[]; kol6=[]; kol7=[]; kol8=[]; kol9=[]; kol10=[]; kol11=[]; kol12=[]; kol13=[]; kol14=[]; kol15=[]; kol16=[]; kol17=[]; kol18=[]; kol19=[]; kol20=[]
    for a in range(1,x+1):
        kol1.append(1)
        for b in range(1,a+1):
            kol2.append(sum(kol1))
            kol2 = list(set(kol2))
            for c in range(1,b+1):
                kol3.append(sum(kol2))
                kol3 = list(set(kol3))
                for d in range(1,c+1):
                    kol4.append(sum(kol3))
                    kol4 = list(set(kol4))
                    for e in range(1,d+1):
                        kol5.append(sum(kol4))
                        kol5 = list(set(kol5))
                        for e in range(1,d+1):
                            kol6.append(sum(kol5))
                            kol6 = list(set(kol6))
                            for f in range(1,e+1):
                                kol7.append(sum(kol6))
                                kol7 = list(set(kol7))
                                for g in range(1,f+1):
                                    kol8.append(sum(kol7))
                                    kol8 = list(set(kol8))
                                    for h in range(1,g+1):
                                        kol9.append(sum(kol8))
                                        kol9 = list(set(kol9))
                                        for g in range(1,f+1):
                                            kol10.append(sum(kol9))
                                            kol10 = list(set(kol10))
                                            for h in range(1,g+1):
                                                kol11.append(sum(kol10))
                                                kol11 = list(set(kol11))
                                                for i in range(1,h+1):
                                                    kol12.append(sum(kol11))
                                                    kol12 = list(set(kol12))
                                                    for j in range(1,i+1):
                                                        kol13.append(sum(kol12))
                                                        kol13 = list(set(kol13))
                                                        for k in range(1,j+1):
                                                            kol14.append(sum(kol13))
                                                            kol14 = list(set(kol14))
                                                            for l in range(1,k+1):
                                                                kol15.append(sum(kol14))
                                                                kol15 = list(set(kol15))
                                                                for m in range(1,l+1):
                                                                    kol16.append(sum(kol15))
                                                                    kol16 = list(set(kol16))
                                                                    for n in range(1,m+1):
                                                                        kol17.append(sum(kol16))
                                                                        kol17 = list(set(kol17))
                                                                        for o in range(1,n+1):
                                                                            kol18.append(sum(kol17))
                                                                            kol18 = list(set(kol18))
                                                                            for p in range(1,o+1):
                                                                                kol19.append(sum(kol18))
                                                                                kol19 = list(set(kol19))
                                                                                for q in range(1,p+1):
                                                                                    kol20.append(sum(kol19))
                                                                                    kol20 = list(set(kol20))
        il+=1
        print(il)

    wynik = 2*(kol1[-1]+kol2[-1]+kol3[-1]+kol4[-1]+kol5[-1]+kol6[-1]+kol7[-1]+kol8[-1]+kol9[-1]+kol10[-1]+kol11[-1]+kol12[-1]+kol13[-1]+kol14[-1]+kol15[-1]+kol16[-1]+kol17[-1]+kol18[-1]+kol19[-1]+kol20[-1])
    return wynik
print(grid(20))