import math

class Calculator:

  def add(self, a, b):

     return a + b

  def subtract(self, a, b):

     return a - b

  def multiply(self, a, b):

     return a * b

  def divide(self, a, b):

     return a / b

# TODO: Implement the following function to calculate the square root of a number.

 def square_root(self, x):

     return math.sqrt(x)

# You need to uncomment the above function and complete its implementation to add the square root feature.

if __name__ == "__main__":

 calculator = Calculator()

num1 = 16

num2 = 4

print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 

print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

# TODO: Implement the following function to calculate the square root of a number.

 def square_root(self, x):

     return math.sqrt(x)
