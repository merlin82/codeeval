import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    a,b = test.strip().split(';')
    c = set(a.split(',')).intersection(set(b.split(',')))
    print ','.join(sorted(list(c)))
test_cases.close()

