lst = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
lst = lst.split()
lst2 = []
x=1

tym = []
for a in lst:
    a = int(a)
    tym.append(a)
    if len(tym) == x:
        lst2.append(tym)
        tym = []
        x+=1
ind1 = len(lst2)-1
while ind1>=0:
    for a in range(0,len(lst2[ind1])-1):
        if lst2[ind1][a]>lst2[ind1][a+1]:
            lst2[ind1-1][a]+=lst2[ind1][a]
        else:
            lst2[ind1-1][a]+=lst2[ind1][a+1]
    ind1-=1
print(lst2[0][0])


