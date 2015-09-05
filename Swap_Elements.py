import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    l, swaps = test.split(":")
    swaps = swaps.split(",")
    l = l.split()
    for s in swaps:
        s = s.strip().split("-")
        s = [int(x) for x in s]
        l[s[0]], l[s[1]] = l[s[1]], l[s[0]]
        
    print ' '.join(l)
test_cases.close()

