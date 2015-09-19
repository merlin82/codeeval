import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    yes = True
    for i, c in enumerate(test):
        if int(c) != test.count(str(i)):
            print 0
            yes = False
            break
    if yes:
        print 1
test_cases.close()

