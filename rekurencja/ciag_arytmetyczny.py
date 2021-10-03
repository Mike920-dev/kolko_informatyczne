def ciag_arytmetyczny_iter(n, a, r):
    i = 1
    # i < n, bo 5 jest już pierwszym wyrazem
    while i < n:
        a += r
        i += 1
    return a

# 1. sposób rekurencją
def ciag_arytmetyczny_recursive(n, a, r):
    # n == 1, bo 5 jest pierwszym elementem
    if n == 1:
        return a
    if n > 0:
        a += r
        n -= 1
        return ciag_arytmetyczny_recursive(n, a, r)

# 2. sposób rekurencją
def ciag_arytmetyczny_recursive2(n, a, r, i=1):
    # i >= n, bo 5 to pierwszy element ciągu
    if i >= n:
        return a
    if i < n:
        a += r
        i += 1
        return ciag_arytmetyczny_recursive2(n, a, r, i)


n = int(input("Podaj n-ty element ciągu, który chcesz wyświetlić n:"))
a = int(input("Podaj wartość początkową ciągu(1. element) a:"))
r = int(input("Podaj różnicę r:"))
print(f'Ciąg arytmetyczny iteracyjnie: {ciag_arytmetyczny_iter(n, a, r)}') # 8
print(f'Ciąg arytmetyczny rekurencyjnie: {ciag_arytmetyczny_recursive(n, a, r)}') # 8
print(f'Ciąg arytmetyczny rekurencyjnie: {ciag_arytmetyczny_recursive2(n, a, r)}') # 8