import sys
     
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    a,b = test.split(' ')

    a = int(a[0:2])*3600+int(a[3:5])*60+int(a[6:8])
    b = int(b[0:2])*3600+int(b[3:5])*60+int(b[6:8])
    c = abs(a-b)
    print "%02d:%02d:%02d"%(c/3600,(c/60)%60, c%60)
test_cases.close()

