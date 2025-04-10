# to get input from the user
age = int(input("Enter your Age : "))

remain_days = 365*(90-age)
remain_month = 12*(90-age)
remain_weeks = 52*(90-age)

print(f"You have {remain_days} Days , {remain_weeks} weeks and {remain_month} months left")