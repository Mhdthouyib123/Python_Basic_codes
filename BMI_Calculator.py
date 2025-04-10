# to get input from user.
weight = int(input("Enter your weight in kg : "))
height = float(input("Enter your Height in m : "))

# to calculate BMI using its formula & convert it into a integer.
Body_Mass_Index = int(weight/height**2)
print("Your BMI is " , Body_Mass_Index)
