import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n,p1,p2 = test.strip().split(',')
    n,p1,p2 = int(n),int(p1)-1,int(p2)-1
    if (n & (1 << p1)) >> p1 == (n & (1 << p2)) >> p2:
        print 'true'
    else:
        print 'false'
test_cases.close()

