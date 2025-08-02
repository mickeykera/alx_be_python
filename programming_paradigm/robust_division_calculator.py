def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    try:
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    