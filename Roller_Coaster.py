import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    l = []
    i = 0
    for c in test:
        if c.isalpha():
            if i % 2 == 0:
                l.append(c.upper())
            else:
                l.append(c.lower())
            i+=1
        else:
            l.append(c)
    print ''.join(l)
test_cases.close()

