import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split(';')
    l = [0,]
    for t in test:
        if t == '':
            continue
        city, dist = t.split(',')
        l.append(int(dist))
    l.sort()
    r = []
    for i in range(1,len(l)):
        r.append(str(l[i]-l[i-1]))
    print ','.join(r)
test_cases.close()

