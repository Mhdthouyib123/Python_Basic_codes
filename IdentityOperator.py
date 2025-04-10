# to assign values to the variable.
a = 5
b = 5

# to perform identity operation.
print(a is b)
print(a is not b)

# to check id or memory address.
print(id(a))
print(id(b))

# difference b/w '==' & 'is' , both are same? 
# no the 'is' based on the same memory address. '==' based on the equalent value only.
# normally the output is same but operation is different.

r = 6
t = '6'

print(r == t)
print(r is t)

print(id(r))
print(id(t))