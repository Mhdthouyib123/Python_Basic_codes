# to get input from user
order = input("Enter Your Pizza Size[S/M/L] : ")
bill = 0

# bill printing using conditions
if order == 'S' or order == 's':
    bill = 100
    pep = input("You need to add peproni?[Y/N] : ")
    if pep == 'Y' or pep == 'y':
        bill = bill + 30
    elif pep == 'N' or pep == 'n':
        bill = bill
elif order == 'M' or order == 'm':
    bill = 200
    pep = input("You need to add peproni?[Y/N] : ")
    if pep == 'Y' or pep == 'y':
        bill = bill + 50
    elif pep == 'N' or pep == 'n':
        bill = bill
elif order == 'L' or order == 'l':
    bill = 300
    pep = input("You need to add peproni?[Y/N] : ")
    if pep == 'Y' or pep == 'y':
        bill = bill + 50
    elif pep == 'N' or pep == 'n':
        bill = bill

cheese = input("You need to add Extra Cheese?[Y/N] : ")

if cheese == 'Y' or cheese == 'y':
    bill = bill + 20
elif cheese == 'N' or cheese == 'n':
    bill = bill

print("Your Total Bill is ",bill)
