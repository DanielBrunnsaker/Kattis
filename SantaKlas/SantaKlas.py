import math
import sys

#file = open('votes.txt', 'r')

for line in sys.stdin:

    temp = line.split(' ')
    
    altitude = int(temp[0])
    angle = int(temp[1])

    if angle >= 0 and angle <= 180:
        print('safe')
    else:
        distance = altitude/math.sin(math.radians(angle))
        print(int(-distance))