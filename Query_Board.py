import sys

lists = [[0 for i in range(256)] for i in range(256)]
          
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().split()
    if test[0] == 'SetCol':
        for i in range(256):
            lists[i][int(test[1])] = int(test[2])
    elif test[0] == 'SetRow':
        for i in range(256):
            lists[int(test[1])][i] = int(test[2])
    elif test[0] == 'QueryRow':
        s = 0
        for i in range(256):
            s += lists[int(test[1])][i]
        print s
    elif test[0] == 'QueryCol':
        s = 0
        for i in range(256):
            s += lists[i][int(test[1])]
        print s
    else:
        pass
test_cases.close()

