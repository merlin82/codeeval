import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if len(test) <= 55:
        print test
    else:
        pos = 40
        for i in range(pos-1, 0, -1):
            if test[i] == ' ':
                pos = i
                break;
            
        test = test[:pos]

        test = test.strip()
        print "%s%s"%(test, "... <Read More>")
test_cases.close()
