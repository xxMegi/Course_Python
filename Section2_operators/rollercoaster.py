#age = 12
#height = 150

def rollercoaster(age, height):
    if age >= 10 and height >= 140:
        print("YOU CAN USE ROLLERCOASTER!")
    else:
        print("YOU CANNOT USE ROLLERCOASTER!")

age = int(input("enter your age :"))
height = int(input("enter your height :"))

rollercoaster(age, height)