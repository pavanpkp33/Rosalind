# Author __ PavanKumar Pasala __
from itertools import product

#input_str = "CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG"
pointer=open("file.txt", "r")
input_str = pointer.read().splitlines()
input_str = ''.join(input_str[1:])


# Method to find the cartesian product of 'TAGC' and order it lexicographically
def order_lex():
    # get the cartesian product of elements in list

    items = product('ACGT', repeat=4)
    # for i in items:
    #     print(i)

    cartesian_array = []
    # sort the items lexicographically
    for item in items:
        cartesian_array.append(''.join(item))
    #cartesian_array.sort()
    return cartesian_array




lex_list = order_lex()

#method to split string into 4-mers
def split_input(inputStr):
    split_str = ''
    for i in range(len(inputStr)):
        if len(inputStr[i:i + 4]) > 3:
            split_str += inputStr[i:i + 4] + " "
    return split_str

split_input = split_input(input_str)
count_str = ''
#counting the number of occurences
for i in lex_list:
    count_str += str(split_input.count(i)) + ' '
print(count_str)


