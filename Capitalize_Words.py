import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    test = [x[0].upper()+x[1:] for x in test]
    print ' '.join(test)
test_cases.close()

