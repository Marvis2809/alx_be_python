num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case"*":
        result = num1 * num2
    case "/":
        if num1 or num2 == 0:
            print("Cannot divide by zero.")
            result = None
        else:
            num1 / num2
    case _:
        result = None
if result is not None:
    if isinstance(result, float) and result.is_integer():
        print(f"The result is {int(result)}.")
    else:
        print(f"The result is {result}.")

