import sys

def squares(n):
    s = 0
    for c in str(n):
        s += pow(int(c), 2)
    return s
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n = int(test)
    l = [n]
    while True:
        if n == 1:
            print 1
            break
        else:
            n = squares(n)
            if n in l and n != 1:
                print 0
                break
            else:
                l.append(n)
test_cases.close()

