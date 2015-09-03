def counter(x):
    jed = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,}
    teen = {0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8}
    dzie = {1:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6, 0:0}
    hun = 7
    sum=0
    for a in range(1,x+1):
        a = str(a)
        if int(a)==1000:
            sum+=11
            return sum
        if int(a) < 10:
            sum += jed[int(a[-1])]
        elif int(a[-2]) == 1:
            sum+=teen[int(a[-1])]
        else:
            sum += jed[int(a[-1])]
            if int(a)>9:
                sum+=dzie[int(a[-2])]
        if int(a)>99:
            sum+=jed[int(a[-3])]+hun
        if int(a)%100 != 0 and int(a)>99:
            sum+=3


print(counter(1000))