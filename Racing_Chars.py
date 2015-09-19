import sys

pre_pos = None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    i = test.find('C')
    if i != -1:
        pos = i
    else:
        pos = test.find('_')
    
    if pre_pos is None or pos == pre_pos:
        direction = '|'
    elif pos < pre_pos:
        direction = '/'
    else:
        direction = '\\'
    pre_pos = pos
    print "%s%s%s"%(test[0:pos], direction, test[pos+1:])        
test_cases.close()

