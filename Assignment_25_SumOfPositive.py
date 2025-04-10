# to get input from the user
num = int(input("Enter your number: "))

# to initialize the sum
sum = 0

# to calculate the sum of each number entered by user util user enter to exit
while True:
    if num <= 0:
        print("Exit")
        break
    else:
        sum += num
        num = int(input("Enter your number: "))
print(sum)