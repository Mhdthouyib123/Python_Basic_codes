# to get input from the user
height = input("Enter the heights separated by ',' : ")

# to split the input into a list
new = height.split(',')

# to convert each element in the list into integer
hei = [int(i) for i in new]

# to get the length of the list
count = len(hei)

# initialize the vale of sum
avlis = 0

# to add the element in the list and get average
for j in hei:
    avlis = avlis+j
avg = avlis / count
print(round(avg)) # to round the avg and print it