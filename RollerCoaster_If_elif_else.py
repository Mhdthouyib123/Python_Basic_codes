# to get input from the user
height = int(input("Enter Your Height in feet : "))

# to check the person is eligible to ride the roller coaster
if height > 3 :
    print("You can Ride")
    age = int(input("Enter Your Age : ")) # to get input from the user
    if age < 12 :
        print("Pay 250 Rupees")
    elif age < 18 :
        print("Pay 500 Rupees")
    else :
        print("Pay 750 Rupees")
else :
    print("You are not Eligible to Ride")