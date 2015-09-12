import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = test.split(",")
    l = len(test)
    m = l/2
    found = False
    test.sort()
    i = 0
    while True:
        c = test.count(test[i])
        if c > m:
            print test[i]
            found = True
            break           
        else:
            i += c
            if i == l:
                break

    if not found:
        print "None"
test_cases.close()

