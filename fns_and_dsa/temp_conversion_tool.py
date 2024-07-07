FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)* FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR +32

temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type == "F":
    conversion = convert_to_celsius(temperature)
    print(f"{temperature}°F is {conversion}°C")
elif temperature_type == "C":
    conversion = convert_to_fahrenheit(temperature)
    print(f'{temperature}°C is {conversion}°F')
else:
    print("invalid temperature. Please enter a numeric value")