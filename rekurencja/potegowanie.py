def potegowanie_iter(podstawa, wykladnik):
    wynik = 1
    while wykladnik != 0:
        wynik *= podstawa
        wykladnik -= 1
    
    return wynik

def potegowanie_iter2(podstawa, wykladnik):
    return podstawa ** wykladnik

def potegowanie_recursive(podstawa, wykladnik, wynik=1):
    if wykladnik == 0:
        return wynik
    if wykladnik > 0:
        wynik *= podstawa
        wykladnik -= 1
        return potegowanie_recursive(podstawa, wykladnik, wynik)

print(f'Potęgowanie iteracyjnie: {potegowanie_iter(2, 4)}') # 16
print(f'Potęgowanie iteracyjnie: {potegowanie_iter2(2, 4)}') # 16
print(f'Potęgowanie iteracyjnie: {potegowanie_recursive(2, 4)}') # 16