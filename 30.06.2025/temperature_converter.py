temp = float(input("Enter temperature: "))
unit = input("Celsius (C) or Fahrenheit (F)? ").upper()
if unit == 'C':
    print(f"{temp}°C = {(temp * 9/5) + 32}°F")
elif unit == 'F':
    print(f"{temp}°F = {(temp - 32) * 5/9}°C")
else:
    print("Invalid unit.")