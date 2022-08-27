# python program to make a simple calculator that calculate addition,subtraction, multiplication, division

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

# print Option

print("Select option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from user 

choise = int(input("Enter your choice 1/2/3/4: "))

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number: "))

if choise == 1:
    print("Addition of {} and {} is {} ".format(num1, num2,add(num1, num2))) 

elif choise == 2:
    print("Addition of {} and {} is {} ".format(num1, num2,sub(num1, num2))) 

elif choise == 3:
    print("Addition of {} and {} is {} ".format(num1, num2,mul(num1, num2))) 

elif choise == 4:
    print("Addition of {} and {} is {} ".format(num1, num2,div(num1, num2))) 

else:
    print("Invalid Choise")