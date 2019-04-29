import sys    

tom = []

for line in sys.stdin:
    tal = line.split()
    tom.append(tal)


talen = tom[0]
listbok = tom[1]

bok = [ch for ch in listbok[0]] 

talen = [int(i) for i in talen]


C1 = max(talen); 
A1 = min(talen); 

talen.remove(C1)
talen.remove(A1)

B1 = talen[0]


a = { "A":A1, "B":B1, "C":C1 }
First = (a.get(bok[0]))
Second = (a.get(bok[1]))
Third = (a.get(bok[2]))

print(First, Second, Third)