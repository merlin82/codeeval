import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = float(test.strip())
    angle = int(test)
    minute = (test-angle)*60
    second = (minute-int(minute))*60
    minute = int(minute)
    second = int(second)
    print '%d.%02d\'%02d"'%(angle,minute,second)
    
test_cases.close()

