
lst = open("p26.txt", 'r')
biggest = [0, 0]
for z, line in enumerate(lst):
    x = line.split()
    if int(x[1]) > int(biggest[1]):
        print("Old: ", biggest)
        biggest[0] = x[0]
        biggest[1] = x[1]
        print("New: ", biggest)
    if z == 999:
        break
print(biggest)
