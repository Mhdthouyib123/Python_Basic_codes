# to get input from the user.
a = int(input("Enter your number a : "))
b = int(input("Enter your number b : "))
print("The value for a is " + str(a) + "\n" + "The value for b is " + str(b))

# Assignment operations.

c = a+b
print("Initial value for c is " , c)

a += 5
b += 7
print("The updated value for a is " + str(a) + "\n" + "The updated value for b is " + str(b))

c -= a
print("Upadated value for c in phase 1 is " ,c)
c /= b
print("Upadated value for c in phase 2 is " ,c)
c *= a
print("Upadated value for c in phase 3 is " ,c)
c //= a
print("Upadated value for c in phase 4 is " ,c)
