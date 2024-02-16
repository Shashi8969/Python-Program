# Write a program add.py that takes 2 numbers as command line arguments and prints its sum.
import sys 
def add_numbers(num1, num2): 
 return num1 + num2 
def command_line(): 
    if len(sys.argv) != 3: 
        print("enter only two number") 
        sys.exit(1) 
num1 = float(sys.argv[1]) 
num2 = float(sys.argv[2]) 
result = add_numbers(num1, num2) 
print("The sum is : ",result) 
command_line()