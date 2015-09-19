import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = test.split()

    print ' '.join(sorted(test, reverse=True))
test_cases.close()

