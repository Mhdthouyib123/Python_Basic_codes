# to create 3 rows
row_1 = ['📦','📦','📦']
row_2 = ['📦','📦','📦']
row_3 = ['📦','📦','📦']

# to make a matrix containing these three rows
matrix = [row_1,row_2,row_3]

# to print the initial matrix
print(f"{row_1}\n{row_2}\n{row_3}")

# to get input from the user
num = input("Enter your position[two digits] : ")

# to change the length provided by the user into index
row_selected = int(num[0])-1
column_selected = int(num[1])-1

# to make the provided position with the 'x' letter
matrix[row_selected][column_selected] = 'X'

# to print the updated matrix
print(f"{row_1}\n{row_2}\n{row_3}")
