import itertools
import sys
import math

counter = 0
file = open('votes.txt', 'r')
lines = file.readline()
#lines = sys.stdin.readline()

all = lines.split(' ')

total = int(all[3])
b = int(all[0])
c = int(all[1])
d = int(all[2])

minmum = min(b,c,d)
hmm = total/minmum

#iterables = list(itertools.product(range(int(hmm)+1),repeat = 3))
ji = math.floor(total/b)+1
ii = math.floor(total/c)+1
ki = math.floor(total/d)+1

if b > total and c > total and d > total:
    print('impossible')
    quit

if b%2 and c%2 and d%2 and total%2 == 1:
    print('impossible')
    quit

for j in range(ji):
    for i in range(ii):
        for k in range(ki):
            #print(j,i,k)

            if j*b+i*c+k*d == total:
                print(j,i,k)
                counter += 1
if counter == 0:
    print('impossible')
            

'''
saved = []
for j in range(len(iterables)):

    bx = b*int(iterables[j][0])
    cx = c*int(iterables[j][1])
    dx = d*int(iterables[j][2])


    if bx+cx+dx == total:
        counter += 1
    
        print(iterables[j][0],iterables[j][1],iterables[j][2])

if counter == 0:
    print('impossible')
    '''