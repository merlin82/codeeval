import sys
def pos(x,y):
    return chr(ord('a')+x-1)+str(y)
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    x = ord(test[0])-ord('a')+1
    y = int(test[1])
    l = []
    if x-1 >0:
        if y-2>0:
            l.append(pos(x-1,y-2))
        if y+2<9:
            l.append(pos(x-1,y+2))    
    if x-2 >0:
        if y-1>0:
            l.append(pos(x-2,y-1))
        if y+1<9:
            l.append(pos(x-2,y+1))       
    if x+1 < 9:
        if y-2>0:
            l.append(pos(x+1,y-2))
        if y+2<9:
            l.append(pos(x+1,y+2))    
    if x+2 < 9:
        if y-1>0:
            l.append(pos(x+2,y-1))
        if y+1<9:
            l.append(pos(x+2,y+1))
    l.sort()
    print' '.join(l)                  
test_cases.close()
