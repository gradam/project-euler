__author__ = 'Kuba'

maxy = {'number': 0, 'qty': 0}
for p in range(1, 1001):
    count = 0
    for c in range(p//3, p//2):
        for a in range(1,  c + 1):
            b = p - c - a
            if a**2+b**2 == c**2:
                count += 1
    count /= 2
    if count > maxy['qty']:
        maxy['qty'] = count
        maxy['number'] = p

print(maxy)

