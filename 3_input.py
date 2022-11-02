# Handling input in python
# The input function allows use to input data and store it in a variable

print("User profile application")

first_name = input("First Name: ")
last_name = input("Last Name: ")
occupation = input("Your Job")

print("Your first name is" + first_name)
print("Your last name is" + last_name)
print("Your Job is" + occupation)

# Another way of outputing information in python in is through formatted strings
print(f"Your first name is {first_name} and your job is {occupation}")

# Handling non-string input
age = int(input("please enter your age: "))
print(f"In two years, your age will be {age+2}")
