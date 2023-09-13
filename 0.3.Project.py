# prompt for the first operand
operand1 = float(input("Enter the first operand:"))

# prompt for the operator
operator = input("Enter an operator(+,-,*,/):")

# prompt for the second operand
operand2 = float(input("Enter the second operand:"))

# calcuate the result based on the operator
if operator == "+":
    result = operand1 + operand2
elif operator == "-":
    result = operand1 - operand2
elif operator == "*":
    result = operand1 * operand2
elif operator == "/":
    result = operand1 / operand2
else:
    print("invalid operator")

# display the result of operand1, operator, and operand2 for the result of the calculation
print(f"{operand1} {operator} {operand2} = {result}")