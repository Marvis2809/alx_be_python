num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invaild operation.")
    result = None

if result is not None:
    if isinstance(result, float) and result.is_integer():
        print(f"The result is {int(result)}.")
    else:
        print(f"The result is {result}.")

