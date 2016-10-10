


seq = input("Enter the sequence")
sub = input("Enter string to be searched")
pos = ''
for i in range(1,len(seq)):
    if seq[i:i+len(sub)] == sub:
        pos += str(i+1)+' '

print(pos)
