suma = 0
p200 = 200
p100 = 100
p50 = 50
p20 = 20
p10 = 10
p5 = 5
p2 = 2
p1 = 1
ilosc = 0


for a in range(0, 2):
    for b in range(0, 3):
        for c in range(0, 5):
            for d in range(0, 11):
                for e in range(0, 21):
                    for f in range(0, 41):
                        for g in range(0, 101):
                            for h in range(0, 201):
                                hej = a*p200 + b*p100 + c*p50 + d*p20 + e*p10 + f*p5 + g*p2 + h*p1
                                if hej == 200:
                                    ilosc += 1
                                elif hej > 200:
                                    break
print(ilosc)