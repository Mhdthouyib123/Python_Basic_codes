# to get input from the user
height = int(input("Enter Your Height in feet : "))

# initially assign  bill is 0
bill = 0

# to check the person is eligible to ride the roller coaster
if height > 3 :
    print("You can Ride")
    age = int(input("Enter Your Age : ")) # to get input from the user
    if age < 12 :
        bill = 250
        print("Pay 250 Rupees")
    elif age < 18 :
        bill = 500
        print("Pay 500 Rupees")
    else :
        bill = 750
        print("Pay 750 Rupees")

    photo_charge = input("You need Photo [Y/N] : ") # to check they need photo or not & also provide total bill
    if photo_charge == 'y' or photo_charge == 'Y' :
        bill = bill + 100 
        print(f"Your Total Bill is {bill}")
    elif photo_charge == 'n' or photo_charge == 'N' :
        print(f"Your Total Bill is {bill}")
else :
    print("You are not Eligible to Ride")