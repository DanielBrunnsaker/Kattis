import sys

def shift_n_letters(letter, n):
    return chr((ord(letter) - 97 + n % 26) % 26 + 97)


for i in sys.stdin:
    lngth = int(len(i)-1)

    txt = list(i.lower())

    first = txt[0:int(lngth/2)]
    second = txt[int(lngth/2):int(lngth)]

    rotation_first = 0
    rotation_second = 0

    tot = []

    for k in range(int(lngth/2)):

        #convert to number
        value_first = ord(first[k])%32-1
        value_second = ord(second[k])%32-1
        #sum
        rotation_first += value_first
        rotation_second += value_second
    
    #rotation
    for j in range(int(lngth/2)):
        
        letter_first = shift_n_letters(first[j], rotation_first)
        letter_second = shift_n_letters(second[j], rotation_second)

        tot += shift_n_letters(letter_first, ord(letter_second)%32-1)

    print((''.join(tot).upper()))
    


