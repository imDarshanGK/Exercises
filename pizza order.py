bill = 0

while True:  # Loop for valid pizza size
    size = input("Enter size of pizza you want (S/M/L): ").lower()

    if size == 's':
        bill += 100
        print("Small pizza price is 100 Rs.")
        break
    elif size == 'm':
        bill += 200
        print("Medium pizza price is 200 Rs.")
        break
    elif size == 'l':
        bill += 300
        print("Large pizza price is 300 Rs.")
        break
    else:
        print("Please enter a valid size!")

while True: # Loop for valid pepperoni choice
    add_pepperoni = input("Do you want pepperoni (Y/N)? ").lower()
    
    if add_pepperoni == 'y':
        if size == 's':
            bill += 30
        else:
            bill += 50
        break
    elif add_pepperoni == 'n':
        break
    else:
        print("Please enter a valid option (Y/N)!")

while True: # Loop for valid extra cheese choice
    extra_cheese = input("Do you want extra cheese (Y/N)? ").lower()
    
    if extra_cheese == 'y':
        bill += 20
        break
    elif extra_cheese == 'n':
        break
    else:
        print("Please enter a valid option (Y/N)!")

print(f"Your final bill is {bill} Rs.")
