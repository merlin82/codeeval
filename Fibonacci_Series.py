import sys
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test.strip())
    print fib(test)
test_cases.close()

