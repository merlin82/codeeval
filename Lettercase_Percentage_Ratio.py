import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    i = 0.0
    for c in test:
        if c.isupper():
            i+=1.0
    
    up = i/len(test)*100
    print "lowercase: %.2f uppercase: %.2f"%(100-up, up)
test_cases.close()

