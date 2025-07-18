num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)
    case _:
        print("Invalid operation")
print("The result is: ", num1, operation, num2)

