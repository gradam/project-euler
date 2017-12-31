from primesieve import primes
from collections import defaultdict

def check_collection(values):
    for i, value in enumerate(values):
        if i > len(values) - 3:
            continue
        for n_value in values[i+1:]:
            diff = n_value - value
            if value + diff*2 in values:
                return value, n_value, value + diff*2



data = defaultdict(list)
for x in primes(1000, 9999):
    data[tuple(sorted(str(x)))].append(x)

for value in data.values():
    if len(value) < 3:
        continue
    answer = check_collection(value)
    if answer is not None:
        print(''.join([str(x) for x in answer]))
