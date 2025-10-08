def blood_donation(age,weight):
    if age >= 18:
        if weight >= 50: print("You can donate blood")
        else: print("You can not donate blood - you weigh too little")
    else: print("You can not donate blood - you are too young")


age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))