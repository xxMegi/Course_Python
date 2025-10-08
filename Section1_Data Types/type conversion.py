decimalNum = 45.6789
wholeNum = int(decimalNum)
print(wholeNum, type(wholeNum))

string1 = "4321"
newInt = int(string1)
print(type(newInt))

wholeNum2 = 123
newFloat = float(wholeNum2)
print(newFloat, type(newFloat))

string2 = "96.76"
newFloat2 = float(string2)
print(newFloat2, type(newFloat2))

print(str(wholeNum2) + "to liczba, która składa się z cyfr: "+ str([1,2,3]))