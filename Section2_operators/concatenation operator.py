firstName = "Adam"
lastName = "Nowak"
fullName = firstName + " " + lastName
print(fullName)

listOne = [1,2,3]
listTwo = [4,5,6]
combinedList = listOne + listTwo
print(combinedList)

if len(combinedList) > 5:
    print("The list is long")

greeting = "Hello" + fullName
if "Hello" in greeting:
    print(greeting)