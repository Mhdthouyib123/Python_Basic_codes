# to get input from user
year = int(input("Enter the year : "))

# to check the year is a leap year
if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 == 0:
            print("The Year is a Leap Year")
        else :
            print("The year is not a leap year")
    else :
        print("The Year is a Leap Year")
else :
    print("The year is not a leap year")