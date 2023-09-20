# Task 1 - Compute the max value inside a list of numbers (two ways to do this)
t1_num_list = [1, 2, 4, 8, 16]
t1_max_val = max(t1_num_list)
print(t1_max_val)

t1_max_val_manual = t1_num_list[0]
for number in t1_num_list:
    if number > t1_max_val_manual:
        t1_max_val_manual = number
print(t1_max_val_manual)

# Task 2 - Create an empty list, ask the user to give 5 numbers, and print the average
t2_list = []
for i in range(5):
    t2_list.append(float(input("Please enter a number:\n")))

t2_average = sum(t2_list) / len(t2_list)
print("The values in the list are: " + str(t2_list) + "\nAnd the average of the list is: " + str(t2_average))
    

# Create an empty list, ask the user to give numbers, stop when the number is 0 and print the average
t3_list = []
while True:
    t3_num = int(input("Please input a number:\n"))
    if t3_num == 0:
        break
    t3_list.append(t3_num)

t3_average = sum(t2_list) / len(t2_list)
print("The values in the list are: " + str(t3_list) + "\nAnd the average of the list is: " + str(t3_average))