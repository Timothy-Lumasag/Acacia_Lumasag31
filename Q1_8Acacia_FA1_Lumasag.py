import math # To make the function sqrt() and pow() work.

x1 = float(input("Enter coordinate1 X:")) # Coordinates
y1 = float(input("Enter coordinate1 Y:"))
x2 = float(input("Enter coordinate2 X:"))
y2 = float(input("Enter coordinate2 Y:"))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) # Solution of the Question. 
# The math.sqrt funcion roots the solutions in it.
# The pow.


print(f"The Distance between the coordnates is, {distance:.2f}") # Round up to the nearest 2 decimals, so that there are only 2 decimal places.


# Reflection
# Why is using a library more practical than writing all calculations from scratch? Explain briefly using your activity as an example.
# Using library as a way to make the coding easier. Starting from scratch is hard without any help, and it may be more confusing. That is why 
# relying on libraries help, because they have pre-programmed functions.