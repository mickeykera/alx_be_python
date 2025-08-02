def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
    except ValueError:
        print("Error: Invalid numerator")
    try:
        denominator = float(denominator)
    except ValueError:
        print("Error: Invalid denominator")
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    