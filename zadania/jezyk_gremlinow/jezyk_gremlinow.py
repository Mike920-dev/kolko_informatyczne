def z_grem_na_dzies(liczba):
    if ':' not in liczba:
        return liczba
    elif len(liczba.split(":")) == 2: # jeśli mamy tylko 2 elementy w napisie, np. [1:23] to ostatni zamianiamy na zera
        liczba = liczba.split(":")
        liczba[1] = "0" * int(liczba[1])

        return "".join(liczba)
    else:
        liczba = liczba.split(":")
        
        if not any(len(element) > 1 for element in liczba): # jesli dlugosc któregokolwiek z elementow nie jest wieksza od 1, to zamieniamy na zera 
            for i in range(1, len(liczba), 2): 
                liczba[i] = "0" * int(liczba[i])
        else:
            for i in range(1, len(liczba), 2):
                # if len(liczba[i]) > 1: # pomija elementy o długości większej od 1
                #     continue            
                 # jeśli jest mniejsza od 1 to zamieniamy to na zera
                liczba[i] = "0" * int(liczba[i])

    return "".join(liczba)

def z_dzies_na_grem(liczba):
    liczba=str(liczba)
    liczba = [i for i in liczba]
    x=0
    ile=0
    tmp=False
    while x<len(liczba) :
        if liczba[x]=='0':
            ile+=1
            liczba.pop(x)
            tmp=True
        elif liczba[x]!='0' and tmp:
            if ile>=3: liczba.insert(x,':'+str(ile)+':')
            else: liczba.insert(x,'0'*ile)
            tmp=False
            ile=0
            x+=1
        else: x+=1
    if tmp:
        if ile >= 3: liczba.insert(x, ':' + str(ile))
        else: liczba.insert(x, '0' * ile)
    return "".join(liczba)

n = int(input())

liczby = []

for _ in range(2*n):
    liczby.append(input())

pary = []

for i in range(1, len(liczby), 2):
    pary.append([int(z_grem_na_dzies(liczby[i - 1])), int(z_grem_na_dzies(liczby[i]))])

print()
for para in pary:
    suma = sum(para)

    print(z_dzies_na_grem(str(suma)))
