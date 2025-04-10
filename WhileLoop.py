# to get input from the user
num = int(input("Enter your number [-1 to exit]: "))

# to initialize the sum
sum = 0

# to calculate the sum of each number entered by user util user enter to exit
while True:
    if num == -1:
        print("Exit")
        break
    else:
        sum += num
        print(sum)
        num = int(input("Enter your number [-1 to exit]: "))