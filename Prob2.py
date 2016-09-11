__author__ = 'PavanKumar Pasala'


def count_atgc(str):
    d = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    for letter in str:
        if letter == 'A':
            d['a'] += 1
        elif letter == 'C':
            d['c'] += 1
        elif letter == 'G':
            d['g'] += 1
        elif letter == 'T':
            d['t'] += 1
        else:
            print("invalid sequence found")
    return d


seq = input("Enter the sequence: ")
dic = count_atgc(seq)
print(dic['a'], dic['c'], dic['g'], dic['t'])
