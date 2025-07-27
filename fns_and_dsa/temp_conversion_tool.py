FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

degree = float(input("Enter the temperature to convert: "))
Celsius_or_Fahrenheit = (input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

match Celsius_or_Fahrenheit:
    case "C":
        fahrenheit = convert_to_fahrenheit(degree)
        print(f"{degree}°C is {fahrenheit:.1f}°F")
    case "F":
        celsius = convert_to_celsius(degree)
        print(f"{degree}°F is {celsius:.1f}°C")
    case _:
        print("Invalid temperature. Please enter a numeric value.")
