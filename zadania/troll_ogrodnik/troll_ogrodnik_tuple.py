# Pobranie danych
nm = input().split()
n = int(nm[0])
m = int(nm[1])

# pobranie ilosci owocow i zamiana ich ze stringow na inty(krotka)
skrzynki = input().split()
skrzynki = tuple(map(int, skrzynki))

# pobranie par [x, y] zapytań
zapytania = [input().split() for i in range(m)]

# Zwracanie ilosci owocow z poszczegolnych skryznek
for i in range(m):
    index1 = int(zapytania[i][0]) - 1
    index2 = int(zapytania[i][1])

    suma = sum(skrzynki[index1:index2])

    print(suma)