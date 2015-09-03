def Sundays(y, x):
    ilo = -5
    sun = 0
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for a in range(y, x + 1):
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            dni[1] = 29
        for z in dni:
            ilo += z
            if ilo % 7 == 0:
                sun += 1
        dni[1] = 28
    return sun


print(Sundays(1901, 2000))