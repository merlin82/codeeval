import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().lower()
    beauty_dict = {}
    for c in test:
        if not c.isalpha():
            continue
        if c in beauty_dict:
            beauty_dict[c] += 1
        else:
            beauty_dict[c] = 1
    l = beauty_dict.values()
    l.sort(reverse=True)
    n = 26
    s = 0
    for i in l:
        s += i*n
        n -= 1
    print s
test_cases.close()
