temperature = int(input("Input the temperature: "))
unit = input("(C)Celsius or (F)Fahrenheit: ")
print(type(temperature))

if unit.upper() == "C":
    converted = (temperature * 9/5) + 32
    print(f"The new temperature is {converted}Fahrenheit")
else:
    converted = (temperature - 32) * 5/9
    print(f"The new temperature is {converted} Fahrenheit")
