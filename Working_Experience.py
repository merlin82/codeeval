import sys

month = ['Jan',
'Feb',
'Mar',
'Apr',
'May', 
'Jun',
'Jul',
'Aug',
'Sep',
'Oct',
'Nov',
'Dec']

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    exp = [0 for i in range(360)]
    test = test.strip().split(';')
    for period in test:
        begin, end = period.strip().split('-')
        begin_month, begin_year = begin.split()
        end_month, end_year = end.split()
        begin = month.index(begin_month)+(int(begin_year)-1990)*12
        end = month.index(end_month)+(int(end_year)-1990)*12+1
        for i in range(begin,end):
            exp[i]=1
    
    print exp.count(1)/12
test_cases.close()
