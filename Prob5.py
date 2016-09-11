__author__ = 'PavanKumar Pasala'

# method to complement the DNA Strand

def complement(str):
    # Create a complement dictionary
    complement_dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    # Reverse the Input String
    comp_str = ''
    reversed_string = str[::-1]

    for letter in reversed_string:
        comp_str = comp_str + complement_dic[letter]

    print(comp_str)


seq = input("Enter the sequence to be complemented: ")
complement(seq)

