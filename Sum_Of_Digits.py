import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    s = 0
    for c in test:
        s += int(c)
    print s
test_cases.close()

