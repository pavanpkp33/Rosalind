from Bio.Seq import translate
#small_dataset = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def findATG(dataset):
    list_of_ATG = []
    for i in range(len(dataset)):
        if dataset[i:i+3] == "ATG":
            list_of_ATG.append(dataset[i:])

    return list_of_ATG

small_dataset = input("Enter the string")

setA = findATG(small_dataset)
setB = findATG(reverse_complement(small_dataset))
dna_trans = []
for i in setA:
    dna_trans.append(translate(i, table=1))
for i in setB:
    dna_trans.append(translate(i, table=1))

str_list = []

for i in dna_trans:
    for j in range(len(i)):
        if i[j] == "*":
            str_list.append(i[:j])
            break

final_list = set(str_list)


for i in final_list:
    print(i)




