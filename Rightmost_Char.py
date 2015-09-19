import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s,t = test.strip().split(',')
    print s.rfind(t.strip())
test_cases.close()

