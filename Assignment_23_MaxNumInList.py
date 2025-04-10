# to get input from the user
num = input("Enter your Numbers (separated by ',') : ")
new = num.split(',') # to split the string into list
# method 1
upd = [int(i) for i in new] # to change string element stored in list into integer
print(max(upd)) # to print max using max method

# method 2
max = upd[0] # initialize the max value
# to find the max value using forloop
for j in upd:
    if j > max:
        max = j
print(max)