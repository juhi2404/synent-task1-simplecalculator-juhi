# Simple Calculator (CLI)

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"


# Main program
print("Simple Calculator")
print("Operations: +  -  *  /")

try:
    # Taking input from user
    num1 = float(input("Enter first number: "))
    op = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    # Calling function
    result = calculate(num1, num2, op)

    # Display result
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")
