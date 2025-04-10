# create a list & print it
num = [75,85,94,21,7,5,6,8,24,5,100,36,211,122,4]
print(num)

# to return values from the list
print(num[5],num[8],num[12],sep="\n")

# to sort the list
num.sort()
print(num)

# to reverse the list
num.reverse()
print(num)

# to add elements using append 
num.append(20)
num.append(0)
print(num)

# to add elements using insert
num.insert(0,1000)
num.insert(3,5000)
print(num)

# to add multiple elements using extend
num.extend([2000,3000,7000,8000])
print(num)

# to get a sub list from the list 
print(num[5:10])
print(num[0:3])
print(num[:7])
print(num[0:])
print(num[0:10:2])
print(num[1:10:4])

# to get count of a element
print(num.count(5))
print(num.count(1000))

# to get the total length of the list 
print(len(num))

# to get index of a element in the list 
print(num.index(5))
print(num.index(2000))

# to get or print the copy of the list
print(num.copy())

# to delete a element using remove 
num.remove(2000)
num.remove(1000) # 1000 is the element
num.remove(8000)
print(num)

# to delete a element using pop
num.pop()
num.pop(5) # 5 is index 
print(num)

# to delete all element from the list 
print(num.clear())