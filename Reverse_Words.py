import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    test.reverse()
    print ' '.join(test)
test_cases.close()

