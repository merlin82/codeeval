morse = {".-":"A",
"-...":"B",
"-.-.":"C",
"-..":"D",
".":"E",
"..-.":"F",
"--.":"G",
"....":"H",
"..":"I",
".---":"J",
"-.-":"K",
".-..":"L",
"--":"M",
"-.":"N",
"---":"O",
".--.":"P",
"--.-":"Q",
".-.":"R",
"...":"S",
"-":"T",
"..-":"U",
"...-":"V",
".--":"W",
"-..-":"X",
"-.--":"Y",
"--..":"Z",
"-----":"0",
".----":"1",
"..---":"2",
"...--":"3",
"....-":"4",
".....":"5",
"-....":"6",
"--...":"7",
"---..":"8",
"----.":"9"}

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    words = test.split("  ")
    for word in words:
        letters = word.split()
        str = []
        for l in letters:
            str.append(morse[l])
        
        print ''.join(str),
    print
test_cases.close()

