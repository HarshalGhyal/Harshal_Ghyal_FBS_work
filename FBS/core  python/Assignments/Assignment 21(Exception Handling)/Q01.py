'''Q.1. Develop a simple calculator program that performs basic arithmetic operations (+,
-, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. However, the program should handle the following
exceptions:
a. Invalid Number: If the user enters a number that is not valid, catch the
exception and display an error message.
b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
"/", catch the exception and display an error message.
c. Division by Zero: If the user tries to divide by zero, catch the exception and
display an error message.
Write a program that performs the requested arithmetic operation and
handles the exceptions as described above.'''

def calculator():
    try:
        # --- Read the two numbers ---
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        # --- Read the operator ---
        op = input("Enter operator (+ - * /): ").strip()

        # --- Validate operator ---
        if op not in ("+", "-", "*", "/"):
            raise ValueError(f"Invalid operator '{op}'. Use +, -, * or /.")

        # --- Perform operation ---
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        print(f"\nResult: {num1} {op} {num2} = {result}")

    except ValueError as e:
        # Handles both non-numeric input AND invalid operator
        print(f"\nError: {e}")

    except ZeroDivisionError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    calculator()