import sys

slang =[
', yeah!',
', this is crazy, I tell ya.',
', can U believe this?',
', eh?',
', aw yea.',
', yo.',
'? No way!',
'. Awesome!']
m = 0
i = 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test
    for c in test:
        if c in ['.', '?', '!']:
            if m%2 == 1:
                sys.stdout.write(slang[i%8])
                i += 1
            else:
                sys.stdout.write(c)
            m += 1
        else:
            sys.stdout.write(c)
test_cases.close()
