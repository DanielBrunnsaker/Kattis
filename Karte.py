import sys

infile = sys.stdin

cards = infile.readline()


#cards = 'P01P02P03H02'

cards = [ch for ch in cards]


#pick out cards

kortlek = []
iterator = int(len(cards)/3)

#generating lists of cards
for q in range(iterator):
    A = cards[3*q:3*q+3]
    kortlek.append(A)
#checking for duplicity
    
k = kortlek
new_k = []
for elem in k:
    if elem not in new_k:
        new_k.append(elem)
k = new_k

if len(k) == len(kortlek):
    condition = 0
else:
    condition = 1

if condition == 1:
    print('GRESKA')
else:

    flattened_kortlek = [y for x in kortlek for y in x]

    pcount = flattened_kortlek.count('P')
    misscountp = 13-pcount
    kcount = flattened_kortlek.count('K')
    misscountk = 13-kcount
    hcount = flattened_kortlek.count('H')
    misscounth = 13-hcount
    tcount = flattened_kortlek.count('T')
    misscountt = 13-tcount
    
    print(misscountp, misscountk, misscounth, misscountt)