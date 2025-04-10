# create a Tuple & print it
num = (75,85,94,21,7,5,6,8,24,5,100,36,211,122,4)
print(num)

# to return values from the tuple
print(num[5],num[8],num[12],sep="\n")

# to get a sub tuble from the tuple 
print(num[5:10])
print(num[0:3])
print(num[:7])
print(num[0:])
print(num[0:10:2])
print(num[1:10:4])

# to get count of a element
print(num.count(5))
print(num.count(1000))

# to get the total length of the tuple 
print(len(num))

# to get index of a element in the tuple 
print(num.index(5))

# create anothe tuple
roc = (25,85,74,96,78,3,24,8,5,1,52,71,5681,2,7)

# concadinate the two tuples
new_tuple = roc + num
print(new_tuple)

# to create a tuple with single element
th = (10,)
print(th)
print(type(th))