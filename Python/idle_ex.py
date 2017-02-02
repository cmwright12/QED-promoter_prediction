# you can type your code in a script

# you can use a predefined function from another module
print("Predefined function\n")
import numpy as np
z = [np.sin(x) for x in numbers]
print(z)

# you can define your own function
print("User-defined function\n")

def square(x):
    return x**2

numbers = range(4)
y = [square(n) for n in numbers]
print(y)

# functions can also be used for characters
def add_s(word):
    return word + 's'

print(add_s('fruit'))
print(add_s('deer'))

