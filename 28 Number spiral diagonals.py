y = 1
m = 0
suma = 0
for x in range(1, 501):
    m += 2
    for z in range(1, 5):
        y += m
        suma += y
print(suma+1)