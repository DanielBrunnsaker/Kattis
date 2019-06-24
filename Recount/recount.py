import sys
import statistics

votes = []
numbers = []

for i in sys.stdin:
    votes.append(i)  
try:
    print(statistics.mode(votes))
except:
    print('Runoff!')

