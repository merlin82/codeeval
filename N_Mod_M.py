import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    a, b = test.split(",")
    a = int(a)
    b = int(b)
    print a-a/b*b
test_cases.close()

