import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x,y = test.split(',')
    x = int(x)
    y = int(y)
    z = x/y
    if x%y != 0:
        z += 1
    print y*z
test_cases.close()

