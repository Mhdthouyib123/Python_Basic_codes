# importing random module
import random

# printing number in range 1<= num >=1000
num = random.randint(0,1000) 
print(num)

# printing number in range 1<= num >1000 (1000 is not included)
num = random.randrange(0,1000)
print(num)

# printing float number
num = random.random() # initially it take range 0.0 to 1.0
print(num)
num = random.uniform(5,6) # customize the range 
print(num)

# to print the random value from our set like list , array etc
ch = [50,2,0,21,4,58,7,5,966,82,34,45]
print(random.choice(ch))

# to shuffle the list or array
ch = [50,2,0,21,4,58,7,5,966,82,34,45]
random.shuffle(ch)
print(ch)