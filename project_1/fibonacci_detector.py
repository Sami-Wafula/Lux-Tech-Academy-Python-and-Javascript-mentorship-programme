import sys

def fibonacci(num):
    a = 0
    b = 1
    while b<num:
        c = a+b
        a = b
        b = c
    if b==num or a==num:
        return True
    if b > num:
        return False
    

try:
    num = int(input("Please enter the number you wish to check: "))

except ValueError:
    print("Please enter a valid number.")

try:
     
    
    if fibonacci(num):
        print(f"{num} is a fibonacci number.")
    else:
        print(f"{num} is not a fibonacci number.")

except NameError:
    sys.exit()



 
