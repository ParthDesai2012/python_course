num1 = float(input("Enter the first number- "))
num2 = float(input("Enter the second number- "))
operator = input("Enter the operator- ")

if operator == "+":
    print(f"Result = {num1 + num2}")
elif operator == "-":
    print(f"Result = {num1 - num2}")
elif operator == "*":
    print(f"Result = {num1 * num2}")
elif operator == "/":     
    print(f"Result = {num1 / num2}")
elif operator == "**":
    print(f"Result = {num1 ** num2}")
elif operator == "%":
    print(f"Result = {num1 % num2}")
else:
    print("please enter a valid operator!")