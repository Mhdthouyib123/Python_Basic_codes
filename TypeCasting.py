# simple solution.
name = "Python Code Maker"
length = len(name) # to get the length of the string.
print("Length of the String is",length) # to print the length of the string.

# using typecasting.
name1 = "Python Code Maker"
length1 = len(name1) # to get the length of the string.
print("Length of the String is " + str(length1) + " characters") # to print the length of the string by using concadinate(we also using typecasting to concadinate it).

# checking the data type of elements.
A = "hello guys...."
B = "10"
C = "50"
D = 123
E = 456
F = "500"

# adding elements by typecasting the original.
s1 = int(B)
s2 = int(C)
sum = s1 + s2
print(sum)

# concadinating elements by typecasting the original.
w1 = str(D)
w2 = str(E)
concad = w1 + w2
print(concad)

# adding elements by typecasting the original.
f1 = int(B)
f2 = float(F)
sums = f1 + f2
print(sums)

# to print data type of each element.
print(type(s1))
print(type(s2))
print(type(sum))
print(type(w1))
print(type(w2))
print(type(concad))
print(type(f1))
print(type(f2))
print(type(sums))
print(type(A))