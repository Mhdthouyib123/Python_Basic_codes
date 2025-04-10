# importing random module
import random

# to get input from the user
ip = input("Enter the names of all members separated by ',' : ")

# to split the input string and store as a list
ip_new = ip.split(",")

# to get the random element & print it 
print(f"{random.choice(ip_new)} will pay the bill")