import sys

for line in sys.stdin:
    a = line.split()
    sweet = int(a[0])
    sour = int(a[1])
    
    if sweet+sour == 13:
        print('Never speak again.')
        cond = 0
    else:
        cond = 1
        
    if cond == 1:
        if sweet == sour:
            if [sweet,sour] == [0,0]:
                cond = 0
            else:
                print('Undecided.')
        if sweet < sour:
            print('Left beehind.')
        if sour < sweet:
            print('To the convention.')