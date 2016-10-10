import urllib.request



def url_data(seq):

    url = urllib.request.Request('http://www.uniprot.org/uniprot/'+seq+'.fasta')
    with urllib.request.urlopen(url) as response:
       resp = response.read()
       resp = resp.decode('ascii')

    str_list = []
    str_list = resp.split('\n')

    str_out = ''
    for s in str_list:

        if s!= '' and s[0] != '>':
            str_list += s

    return str_out

def cal_pos(seq):
    out = ''
    for i in range(len(seq)):
        if len(seq[i:i + 4]) > 3:
            if (seq[i] == 'N') and (seq[i+1] != 'P') and (seq[i+2] in ['S','T']) and (seq[i+3] != 'P'):
                out += str(i+1) + ' '
    return out

def read_file(filename):
    pointer = open(filename, 'r')
    contents = pointer.readlines()
    pointer.close()
    return contents

init_dic = {}
list = read_file('file.txt')
for i in list:
    init_dic[i.rstrip()] = ''
    init_dic[i.rstrip()] = cal_pos(url_data(i.rstrip()))

for key, seq in init_dic.items():
    if init_dic[key] != '':
        print(key)
        print(init_dic[key])
