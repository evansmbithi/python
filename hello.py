from datetime import date
import sys

# Today's date
print("Today is:", date.today())

#  One parsec is 3.26 lightyears
parsecs = 11
lightyears = 3.26

lightyears *= parsecs
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# CLI arguments
# $ python hello.py Jupiter Mbithy
# print("Command line arguments:", sys.argv)
# print("Number of arguments:", len(sys.argv))
# print("First argument:", sys.argv[0])
# print("Second argument:", sys.argv[1])
# print("Third argument:", sys.argv[2])

# if expressions
a = 55
b = 33
# test expression
if a > b:
    print("a is greater than b")

# consider the following expression
print("the output is" )

a = 24
b = 44
if a <= 0:
    print(a)
print(b)

print("because the test expression is False and the print(b) statement isn't indented at the same level as the if statement.")

# if..else...elif
a = 55
b = 33
if a <= b:
    print("a is greater than b")
else:
    print("else: b is greater than a")

# elif
a = 93
b = 27
if a == b:
    print("a is equal to b")
elif a >= b:
    print("elif: a is greater than or equal to b")
