__author__ = 'Kuba'
import itertools


def largest():
    for z in itertools.permutations([str(z) for z in range(8, 0, -1)]):
        pandigit = '9' + ''.join(z)
        for index in range(4):
            proba = ''
            number = pandigit[:index + 1]
            for n in range(1, 10):
                proba += str(int(number) * n)
                if proba == pandigit:
                    return pandigit


print(largest())
