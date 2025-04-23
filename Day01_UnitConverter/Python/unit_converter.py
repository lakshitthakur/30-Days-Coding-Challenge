def convert_units():
    print("Welcome to the Unit Converter!")
    print("Choose a conversion type:")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles:.2f} miles.")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == "3":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg is equal to {pounds:.2f} lbs.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    convert_units()
