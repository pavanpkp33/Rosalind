__author__ = 'PavanKumar Pasala'


# method to read input from file

def file_parser(filename):
    pointer = open(filename, 'r')
    contents = pointer.readlines()
    pointer.close()
    return contents


# method to parse the inputs and store it in dictionary
input_dic = {}
fasta_key = ''


def input_parser(input_contents):
    for index in input_contents:
        if index[0] == '>':
            fasta_key = index[1:].rstrip()  # removes all whitespace and new line from input.
            input_dic[fasta_key] = ''  # store the key as reference. Value can be stored next.

        else:
            # store values in corresponding keys
            input_dic[fasta_key] = input_dic[fasta_key] + index.rstrip()
    return input_dic


# method to calculate the GC content

def gc_calculator(sequence):
    count = 0
    for letter in sequence:
        if letter == 'G' or letter == 'C':
            count += 1

    sample_size = len(sequence)
    percentage_gc = (count / sample_size) * 100
    return percentage_gc


gc_values_dict = {}

in_dic = input_parser(file_parser('input.txt'))
for id, seq in in_dic.items():  # loop through input dictionary and get ID, sequence.
    gc_values_dict[id] = gc_calculator(seq)  # calculate the GC value of each sequence and store it with ID.

max_gc_id = max(gc_values_dict, key=gc_values_dict.get)  # Get maximum value of the key

max_gc_value = max(gc_values_dict.values())  # Get maximum value of GC

# Print the values of Key and Value
print(max_gc_id)
print(round(max_gc_value, 7))
