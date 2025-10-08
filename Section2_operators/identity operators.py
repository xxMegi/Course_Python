text = "Hello"
print(text.upper()) # metoda powiększenie liter

x, y = 256, 256
print(x is y)

listOne = [1,2,3]
listTwo = listOne
print(listOne is listTwo) #ten sam obiekt w pamieci

listOne.append(4)
if listOne is not listTwo:
    print("Modification did not affect listTwo")

listThree = [1,2,3,4]
if listOne is listThree:
    print("Both lists are the same") #osobny obiekt w pamieci