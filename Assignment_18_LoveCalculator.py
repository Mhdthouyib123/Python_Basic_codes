# to get input from the user
person_1 = input("Enter Person 1 Name : ").lower()
person_2 = input("Enter Person 2 Name : ").lower()

# to get the sum of count
sum_1 = person_1.count('t') + person_1.count('r') + person_1.count('u') + person_1.count('e') + person_2.count('t') + person_2.count('r') + person_2.count('u') + person_2.count('e')
sum_2 = person_1.count('l') + person_1.count('o') + person_1.count('v') + person_1.count('e') + person_2.count('l') + person_2.count('o') + person_2.count('v') + person_2.count('e')

# typecasting them into string and again into integer
tsum_12 = str(sum_1) + str(sum_2)
tsum_1 = int(tsum_12)

# checking using condition
if tsum_1 >= 80 and tsum_1 <= 100:
    print("perfect Match")
elif tsum_1 >=60 and tsum_1 <=79:
    print("Good Match")
elif tsum_1 >=50 and tsum_1 <=59:
    print("Normal Match")
elif tsum_1 >=40 and tsum_1 <=49:
    print("Adustable Match")
elif tsum_1 >=10 and tsum_1 <=39:
    print("Not Good Match")
elif tsum_1 < 9 :
    print("Never Match")

# printing the score
print("Your Score is ",tsum_1)

