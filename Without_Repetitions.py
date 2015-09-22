import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    l = []
    pre_c = None
    for c in test:
        if pre_c is None or pre_c != c:
            pre_c = c
            l.append(c)
    
    print ''.join(l)
test_cases.close()

