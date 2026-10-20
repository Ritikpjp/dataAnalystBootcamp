from package.maths import *
print(addition(5, 3)) ##this will print the result of the addition function
print(subtraction(5, 3)) ##this will print the result of the subtraction function

from package.subpackages.mult import multiply ##this is how we can import a function from a module in a subpackage in a package.
print(multiply(5, 3)) ##this will print the result of the multiplication function