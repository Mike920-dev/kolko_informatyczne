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
    gremlinska_liczba = ""
    liczba_zer = 0
    nowa_liczba = ""
    stara_max_ilosc = []
    max_ilosc = []
    if "0" not in liczba:
        return liczba

    for i in range(len(liczba)):
        if liczba[i] == "0":
            liczba_zer += 1
        else:
            nowa_liczba += liczba[i]
            liczba_zer = 0
        stara_max_ilosc.append(str(liczba_zer))

     
    stara_max_ilosc = "".join(stara_max_ilosc).split("0")
    
    
    for element in stara_max_ilosc:
        if element not in max_ilosc:
            max_ilosc.append(element)

    for element in max_ilosc:
        if element == '':
            max_ilosc.remove('')

    for i in range(len(max_ilosc)):
        max_ilosc[i] = max(max_ilosc[i])
    
    nowa_liczba = list(nowa_liczba)
    for i in range(len(max_ilosc)):
        nowa_liczba.insert(i, f":{max_ilosc[i]}:")

    return nowa_liczba

    # zera = nowa_liczba[:len(nowa_liczba)//2]
    # liczby = nowa_liczba[len(nowa_liczba)//2:]

    # nowa_liczba_dict = {}
    # for i in range(2*len(nowa_liczba)):
    #     if i == len(liczby):
    #         break
    #     else:
    #         nowa_liczba_dict.update({liczby[i]: zera[i]})
            
    # for num in nowa_liczba_dict:
    #     if int(nowa_liczba_dict[num].strip(":")) < 3:
    #         gremlinska_liczba += num + "0" * int(nowa_liczba_dict[num].strip(":"))
    #     else:
    #         gremlinska_liczba += num + nowa_liczba_dict[num]
    
    # gremlinska_liczba = list(gremlinska_liczba)
    # if gremlinska_liczba[-1] == ":":
    #     gremlinska_liczba.pop(-1)

    # return "".join(gremlinska_liczba)

print(z_dzies_na_grem("123"))
print(z_dzies_na_grem("10030000"))
print(z_dzies_na_grem("100000980000"))
print(z_dzies_na_grem("10002"))
print(z_dzies_na_grem("100020"))
print(z_dzies_na_grem("1000200"))
print(z_dzies_na_grem("102000"))
print(z_dzies_na_grem("1000005"))
print(z_dzies_na_grem("1000500500500505000023"))
print(z_dzies_na_grem("123000403000402"))
print(z_dzies_na_grem("100200030405000600"))

# n = int(input())

# liczby = []

# for _ in range(2*n):
#     liczby.append(input())

# pary = []

# for i in range(1, len(liczby), 2):
#     pary.append([int(z_grem_na_dzies(liczby[i - 1])), int(z_grem_na_dzies(liczby[i]))])

# print()
# for para in pary:
#     suma = sum(para)

#     print(z_dzies_na_grem(str(suma)))
