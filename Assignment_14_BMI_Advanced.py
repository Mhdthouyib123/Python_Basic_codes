weight = int(input("Enter your weight(kg) : ")) # to get weight of user.
height = float(input("Enter your height(m) : ")) # to get height of user.

BMI1 = weight/height**2 # to get BMI(based on its formula).
BMI = round(BMI1,2) # to round the value into 2 decimal.

# to check the category it belongs
if BMI <= 18.5 :
    print(f"Your BMI is {BMI} , it belongs to Under Weight")
elif BMI <= 24.9 :
    print(f"Your BMI is {BMI} , it belongs to Healthy Weight")
elif BMI <= 29.9 :
    print(f"Your BMI is {BMI} , it belongs to Over Weight")
else :
    print(f"Your BMI is {BMI} , it belongs to Obese")
