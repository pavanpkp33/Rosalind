__author__ = 'PavanKumar Pasala'

codon_table = {'A': 4, 'R': 6, 'N': 2, 'D': 2, 'C': 2, 'Q': 2, 'E': 2, 'G': 4, 'H': 2, 'I': 3, 'L': 6, 'K': 2, 'M': 1,
               'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4, '*': 3}

# Method to read the sequence and convert into corresponding codon values
def build_array(sequence):
    codon_array = []
    for i in sequence:
        codon_array.append(codon_table[i])

    return codon_array

def calculate_combinations(arr):
    product = 1

    for number in arr:
        product = product * number  # calculating the product
    product = product * 3           # Multiplying by stop codon which values to 3

    result = product % 1000000      # Modulo of 1000000

    return result


sequence = input("Enter the Sequence")

print(calculate_combinations(build_array(sequence)))