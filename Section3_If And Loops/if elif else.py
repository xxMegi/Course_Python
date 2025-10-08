number = 15

if number > 10:
    print("Number is greater than 10")

if number == 15:
    print("Number is 15")
elif number == 20: print("Number is 20")
elif number == 25: print("Number is 25")
elif number > 30: print("Number is greater than 30")
else:
    print("Another case")

if number > 10:
    print("Number is greater than 10")
    if number % 3 == 0:
        print("Number is divisible by 3")