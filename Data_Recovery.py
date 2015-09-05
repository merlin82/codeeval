import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    words, seq = test.split(";")
    words = words.split()
    seq = seq.split()
    seq = [int(x)  for x in seq]
    for i in range(1, len(words)+1):
        if i not in seq:
            seq.append(i)
            break
    sentence = []
    for i in range(0, len(words)):
        index = seq.index(i+1)
        sentence.append(words[index])
    print ' '.join(sentence)   
     
test_cases.close()

