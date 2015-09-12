import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = test.split(",")
    pre = ''
    l = []
    for i in test:
        if i != pre:
            l.append(i)
            pre = i
    print ','.join(l)
test_cases.close()

