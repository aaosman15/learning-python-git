print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

# testing
# testing 3
try:
    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age? "))
        if age < 12:
            print("Please pay $5")
        elif age <= 18:
            print("Please pay $8")
        else:
            print("Please pay $12")
    else:
        print("Sorry you too short for this")

except Exception as e:
    print(e)
