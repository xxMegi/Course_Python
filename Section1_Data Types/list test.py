list = [0,1,2,3,4,5,6]

print(len(list))
del list[1]
print(len(list))

if 3 in list:
    print("Liczba 3 jest w liście")

for el in list:
    print(el)

for el in list:
    print(el * 2)