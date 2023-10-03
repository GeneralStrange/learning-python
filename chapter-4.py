import os
from c4_own_module import add_2_num

with open("file_test", "r") as f:
    for line in f:
        print (line.rstrip("\n"))

with open("new_file", "a+") as f:
    f.write("change me please\n")

if os.path.exists("new_file"):
    os.remove("new_file")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

print(str(num1) + " + " + str(num2) + " = " + str(add_2_num(num1, num2)))
