"""
Day 10 - Functions with Outputs

You can define functions inside of functions as well as have them standalone
 - def function():
    def inner_function():
       dosomething()
    inner_function()

"""

# Calculator App - Design a calculator that can continue running as needed

def evaluate(val1, val2, op):
    if op == "+":
        return val1 + val2
    if op == "*":
        return val1 * val2
    if op == "/":
        return val1 / val2
    if op == "-":
        return val1 - val2
    return IOError


stop_calculating = False
a = int(input("Enter a number: "))
while not stop_calculating:
    operation = input("Enter operation, +, -, *, /: ")
    b = int(input("Enter a number: "))
    print(f"{a} {operation} {b} = {evaluate(a, b, operation)}")
    stop_calculating = input("Do you want to stop calculating? (y/n): ") == "y"
    a = evaluate(a, b, operation)

print("All done!")
