try:
    temperature = int(input("Input the temperature: "))
    unit = input("(C)Celsius or (F)Fahrenheit: ")

    if isinstance(temperature, int) and unit.upper() == "C":
        converted = (temperature * 9/5) + 32
        print(f"The new temperature is {converted}Fahrenheit")

    elif isinstance(temperature, int) and unit.upper() == "F":
        converted = (temperature - 32) * 5 / 9
        print(f"The new temperature is {converted}Celsius")
except ValueError:
    print("You entered a string, please enter an integer")
