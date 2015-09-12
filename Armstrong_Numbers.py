import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    digits = len(test)
    s = 0
    for c in test:
        s += pow(int(c), digits)
    
    if str(s) == test:
        print True
    else:
        print False
test_cases.close()

