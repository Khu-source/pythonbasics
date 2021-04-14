
import sys 

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print ("Please enter a numerical value.")
    sys.exit(1)

#def division(x, y):
    #return x / y

#print(f"{x} divided by {y} is {division(x, y)}")

try:
    result = x / y
except ZeroDivisionError:
    print ("Denominator cannot be zero")
    sys.exit(1)

print(result)