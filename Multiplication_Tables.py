import sys

for i in range(1,13):
    for j in range(1,13):
        if j == 1:
            sys.stdout.write('%d'%(i*j))
        else:
            sys.stdout.write('%4d'%(i*j))
    print
    
