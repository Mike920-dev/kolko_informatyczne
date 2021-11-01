s = input()
t = int(input())
zapytania = [int(input()) for _ in range(t)]

odp = []

for i in range(t):
    zap = zapytania[i]
    ile = 0
    for j in range(len(s)):
        sl = s[j:zap]
        sl_2 = s[zap:zap+zapytania[i]]
        if len(sl_2) < zapytania[i]:
            break
        if sl == sl_2:
           ile += 1
        zap += 1
    odp.append(ile)

print()
print()


for o in odp:
    print(o)
