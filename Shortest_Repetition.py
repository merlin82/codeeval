import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()

    for i in range(1, len(test)+1):
        if len(test)%i != 0:
            continue
        if i == len(test):
            print i
            break
        
        ok = True
        for j in range(1,len(test)/i):
            if test[0:i] != test[i*j:i*j+i]:
                ok = False
                break
        if ok:
            print i
            break
test_cases.close()

