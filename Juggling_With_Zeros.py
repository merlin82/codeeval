import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    zeros = test.split()
    bin = []
    for i in range(0, len(zeros)-1, 2):
        if zeros[i] == '0':
            bin.append(zeros[i+1])
        else:
            bin.append("1"*len(zeros[i+1]))
    bin = ''.join(bin)
    print int(bin, 2)  
test_cases.close()

