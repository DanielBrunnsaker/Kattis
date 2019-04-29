import sys
lista = []
for line in sys.stdin:
    lista.append(len(line))
    
if lista[0] >= lista[1]:
    print('go')
else:
print('no')