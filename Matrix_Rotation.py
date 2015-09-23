import sys
from math import sqrt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    n = int(sqrt(len(test)))
    matr = [[x for x in test[i*n:i*n+n]] for i in range(n)]
    rotated90 = zip(*matr[::-1])
    for r in rotated90:
        print ' '.join(list(r)),
    print
    
test_cases.close()
