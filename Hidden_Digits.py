import sys

pre_pos = None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    l = []
    for c in test:
        if c.isdigit():
            l.append(c)
        elif c >= 'a' and c <= 'j':
            l.append(str(ord(c)-ord('a')))
        else:
            pass
    if len(l) == 0:
        print 'NONE'
    else:
        print ''.join(l)
test_cases.close()

