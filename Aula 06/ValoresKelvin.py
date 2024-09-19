Kelvin = [255,295,314,354,393,413,453,492,512,552]
Celsius = [round(x - 273.15) for x in Kelvin]
Fahrenheit = [round((x - 273.15) * 9/5 + 32) for x in Kelvin]
print("{:<4}{:<5} {:<8} {:<6}".format("N°", "Kelvin", "Celsius", "Fahrenheit"))
print("__|_______|_______|__________|")
for x in range(len(Kelvin)):
    print("{:<4} {:<5} {:<8} {:<6}".format(x + 1, Kelvin[x], Celsius[x], Fahrenheit[x]))