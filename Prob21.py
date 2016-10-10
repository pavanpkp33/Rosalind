def file_parser(filename):
    pointer = open(filename, 'r')
    contents = pointer.readlines()
    pointer.close()
    return contents

def find_substr(string, list):

    for s in list:
        if (len(s) < len(string)) or (string not in s):
            return False
    return True

contents = file_parser('file.txt')

list = []
input_dic = {}
fasta_key = ''
for index in contents:
    if index[0] == '>':
        fasta_key = index[1:].rstrip()  # removes all whitespace and new line from input.
        input_dic[fasta_key] = ''  # store the key as reference. Value can be stored next.

    else:
        # store values in corresponding keys
        input_dic[fasta_key] = input_dic[fasta_key] + index.rstrip()

for id , seq in input_dic.items():
    list.append(seq)

str_list = []
min_str = min(list)
for i in range(len(min_str)+1):
    for j in range(len(min_str)+1-i):
        for po in range(len(list)):
            if min_str[j:j+i] != '':
                if find_substr(min_str[j:j+i], list):
                    str_list.append(min_str[j:j+i])


print(max(str_list))




