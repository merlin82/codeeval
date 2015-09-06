import sys
import re
from math import sqrt
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = re.split(",|\(|\)| ", test)
    a,b,c,d = [ int(x) for x in test if x != '']
    print int(sqrt((a-c)*(a-c)+(b-d)*(b-d)))
test_cases.close()

