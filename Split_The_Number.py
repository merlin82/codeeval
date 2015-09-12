import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num,pattern  = test.strip().split()
    
    if pattern.find('+') != -1:
        left,right = pattern.split('+')
        left = num[0:len(left)]
        right = num[len(left):]
        print int(left)+int(right)
    else:
        left,right = pattern.split('-')
        left = num[0:len(left)]
        right = num[len(left):]
        print int(left)-int(right)        
test_cases.close()

