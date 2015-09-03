wyn = []
wyn2 = []
wyn3 =[]
g = 1
d = 1
for x in range(10, 100):
    if x % 10 == 0:
        continue
    for z in range(10, 100):
        if z % 10 == 0:
            continue
        m = x/z
        if m > 1 or m == int(m):
            continue
        lst2 = [x, z, m]
        wyn.append(lst2)
for x in range(1, 10):
    for z in range(1, 10):
        if z % 10 == 0:
            continue
        m = x/z
        if m > 1 or m == int(m):
            continue
        lst2 = [x, z, m]
        wyn3.append(lst2)
for x in wyn:
    if str(x[0])[0] == str(x[1])[0]:
        wyn2.append([int(str(x[0])[1]), int(str(x[1])[1]), x[2]])
    if str(x[0])[0] == str(x[1])[1]:
        wyn2.append([int(str(x[0])[1]), int(str(x[1])[0]), x[2]])
    if str(x[0])[1] == str(x[1])[0]:
        wyn2.append([int(str(x[0])[0]), int(str(x[1])[1]), x[2]])
    if str(x[0])[1] == str(x[1])[1]:
        wyn2.append([int(str(x[0])[0]), int(str(x[1])[0]), x[2]])
for x in wyn2:
    for z in wyn3:
        if x == z:
            g *= x[0]
            d *= x[1]
print(g, d)