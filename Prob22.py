def cal_fail(s):
    fail_array = [0 for i in range(len(s))]
    count = len(s)
    pos = 1 # position in the string
    lenlongest = 0 # length of the longest substring

    while pos < count:
        if s[pos] == s[lenlongest]:
            lenlongest += 1
            fail_array[pos] = lenlongest
            pos += 1
        else:
            if lenlongest != 0:
                j = fail_array[lenlongest-1]
            else:
                fail_array[pos] = 0
                pos += 1

    return fail_array

userinput = input("Enter seq")
print(cal_fail(userinput))