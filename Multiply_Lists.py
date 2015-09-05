import sys
import itertools
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    left, right = test.split("|")
    left = left.split()
    right = right.split()

    s = [str(int(x)*int(y)) for x, y in itertools.izip(left, right)]
    print ' '.join(s)

test_cases.close()

