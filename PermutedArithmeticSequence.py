import sys

infile = sys.stdin
next(infile)
for line in infile:
    totdiff = []
    init = line.split()
    
    del init[0]

    lista = [int(i) for i in init]
    sortedlista = sorted(lista)
    sortedlista2 = sorted(lista)

    
    diff = [sortedlista[i+1]-sortedlista[i] for i in range(len(sortedlista)-1)]
    

    sortedlista2.reverse()

    if len(set(diff)) == 1:
        if lista == sortedlista or lista == sortedlista2:
            print('arithmetic')
        if lista != sortedlista and lista != sortedlista2:
            print('permuted arithmetic')
    if len(set(diff)) > 1:
        print('non-arithmetic')