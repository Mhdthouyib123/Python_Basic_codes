# importing random module
import random

# to get input from the user
ip = input("Enter the names of all members separated by ',' : ")

# to split the input string and store as a list
ip_new = ip.split(",")

# to get random element from the list
num = random.randrange(0,len(ip_new))
print(f"{ip_new[num]} will pay the bill")
