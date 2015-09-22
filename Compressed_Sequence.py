import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    pre = None
    c = 1
    for t in test:
        if pre == None:
            pre = t
        elif pre == t:
            c += 1
        else:
            print c,pre,
            pre = t
            c = 1
    print c,t
test_cases.close()

