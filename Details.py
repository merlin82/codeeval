import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(',')
    m = 10
    for t in test:
        d = t.find('Y')-t.rfind('X')-1
        if d < m:
            m = d
    print m
test_cases.close()

