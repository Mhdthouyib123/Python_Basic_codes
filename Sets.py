# to create a set
se = {1,2,4,5,7,889,7,5,4,82,46,84,67,145,45}
print(se)

# to add elements into set
se.add(1000)
print(se)

# to remove element from the set
se.remove(7)
print(se)

# to remove a element from the set using discard method (doesnot return error even if the element is not existing)
se.discard(20)
print(se)

# to add a tuple into a set
se.add((50,47,85,96,45))
print(se)

# to print a empty set and add element to that empty set 
re = set()
print(re)
re.add(5)
print(re)