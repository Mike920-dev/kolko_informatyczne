x = int(input())
y = int(input())

przedzial = [i for i in range(x, y + 1)]

# print([1, 2, 3, 4][1:]) # [2, 3, 4]

ile = 0
trojkaty = []


for i in range(len(przedzial)):
   for j in range(i + 1, len(przedzial)):
      k = 0
      a = przedzial[i]
      b = przedzial[j]
      c = przedzial[j + 1:]

      if k < len(c):
         if a + b > c[k]:
            trojkaty.append((a, b, c))
      ile += 1
      k += 1
      break         
print(trojkaty) # dla 2 i 5 --> [(2, 3, [4, 5]), (2, 4, [5]), (3, 4, [5])]
# print(ile)