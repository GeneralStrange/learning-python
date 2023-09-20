# Task 1 - Ask for the users name and age, and print the info usging a function
def say_hello(user_name, user_age):
    print("Hello " + user_name + ", you are " + {str(user_age)} + " years old.")

say_hello(input("Please tell me your name:\n"), input("And also your age:\n"))

# Task 2 - Using functions ask the user for 2 numbers, add them and print them
def add_two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2

print("The sum of your 2 numbers is: " + str(add_two_numbers()))

# Task 3 - Using functions create a list of 4 float numbers, compute the average and print the result
def sum_list():
    num_list = [1.3, 4.5, 6.9, 9.3]
    average = sum(num_list) / len(num_list)
    print("The values in the list are: " + str(num_list) + "\nAnd the average of the list is: " + str(average))
    
sum_list()