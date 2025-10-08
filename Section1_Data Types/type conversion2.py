numbers = [7, 8, 9, 10, 11, 12]
print(numbers)

tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["hej", 45, 67.895]
print(mixedList)

setMixed = set(mixedList)
print(type(setMixed), setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers), frozenSetNumbers)

nameAgePairs = ( ("Ola",35), ("Adam",25), ("Iga", 19))
ageDict = dict(nameAgePairs)
print(ageDict)
print("Wiek Igi: " + str(ageDict["Iga"]))