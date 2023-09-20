# Task 1 - Ask for the name and age of the user, and print the info
user_name = input("What is your name?\n")
user_age = input("And how old are you " + user_name + "?\n")
print("Thank you " + user_name + ", age " + user_age + "!")

# Task 2 - Ask the user for 2 integer numbers, add them and print them
user_num1 = input("Please tell me a number:\n")
user_num2 = input("And another:\n")
user_sum = int(user_num1) + int(user_num2)
print("Thanks! The sum of these numbers is: " + str(user_sum))

# Task 3 - Create a list of 4 float numbers, compute the average and print the result
num_list = [1.3, 4.5, 6.9, 9.3]
average = sum(num_list) / 4
print("The values in the list are: " + str(num_list) + "\nAnd the average of the list is: " + str(average))