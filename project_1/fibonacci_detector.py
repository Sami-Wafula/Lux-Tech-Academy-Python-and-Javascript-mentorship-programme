'''First assignment for the Lux Tech and Data Science EA Python and Java mentorship programme.
A Fibonacci number detector.
The program will:
a)prompt for user input
b)check the input value against a generated Fibonacci series of values
c)output information wether the input value is Fibonacci or not
Fibonacci logic:F(0) = 0
                F(1) = 1
                F(n) = F(n-1) + F(n-2)'''


def Fibonacci(x):
     n1 = 0
     n2 = 1
     while n2<x:
         n3 = n1+n2
         n1 = n2
         n2 = n3
     if n2==x or n1==x:
         return True
     if n2 > x:
         return False

try:
    x = int(input("Please enter the number you wish to check: "))

except ValueError:
    print("Please enter a valid number.")
except NameError:
     
    
     if Fibonacci(x):
          print(f"{x} is a fibonacci number.")
     else:
          print(f"{x} is not a fibonacci number.")
