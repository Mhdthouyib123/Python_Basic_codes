# to create sets
set1 = {1,2,3,4}
set2 = {3,4,5,6,7}
set3 = {6,7,8,9,0}
# union operation on sets
# method 1
print(set1.union(set2,set3))
# method 2
print(set1 | set2 | set3)

# union update method
# method 1
set1.update(set2)
print(set1)
# method 2
set2 |= set3
print(set2)

set4 = {1,2,3,4,5,8,7,3,1}
set5 = {3,4,5,8,9,7,5,6,7}
set6 = {4,7,5,6,7,8,9,0}

# intersection operation on sets
# method 1
print(set4.intersection(set5))
print(set5.intersection(set6))
print(set5.intersection(set4))
# method 2
print(set4 & set5)
print(set5 & set6)
print(set5 & set3)

# intersection update method
set4.intersection_update(set5,set6)
print(set4)

# intersection update method with list & tuple
set4.intersection_update((100,500,40,20,5,7,9,8))
print(set4)

# to create sets
set01 = {"anu" , "krish" , "gautham" , "mohan"}
set02 = {"dev" , "ben" , "joe" , "anu" , "krish"}
set03 = {"cummings" , "petretod" , "anu" , "ben"}

# difference operation on sets
# method 1
print(set01.difference(set02,set03))

# method 2
print(set01 - set02)

# difference update method
set03.difference_update(set01)
print(set03)

# symmetric difference operation on sets
# method 1
print(set02.symmetric_difference(set03))

# method 2
print(set02 ^ set01)

# symmetric difference update method
set02.symmetric_difference_update(set01)
print(set02)

# to create sets
setA = {1,2,3,4,5}
setB = {1,2,3,4,5,6,7,8,9}
setC = {6,7,8,9,}

# disjoint operation on sets
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

# check a set is a subset of another
# method 1
print(setA.issubset(setB))
print(setA.issubset(setC))

# method 2
print(setA <= setB)
print(setA <= setC)

# check a set is a superset of another
# method 1
print(setA.issuperset(setB))
print(setA.issuperset(setC))

# method 2
print(setA >= setB)
print(setA >= setC)
