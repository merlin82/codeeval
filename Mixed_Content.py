import sys
     
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = test.split(',')
    words = [x for x in test if not x.isdigit()]
    nums = [x for x in test if x.isdigit()]
    if len(words) > 0 and len(nums)> 0:
        print "%s|%s"%(','.join(words),','.join(nums))
    elif len(words) > 0:
        print ','.join(words)
    else:
        print ','.join(nums)
test_cases.close()

