import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = [int(x) for x in test.split()]
    nums = sorted(test)
    found = False
    for i in nums:
        if nums.count(i) == 1:
            print test.index(i)+1
            found = True
            break
    if not found:
        print 0
test_cases.close()

