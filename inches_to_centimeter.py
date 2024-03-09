print("This program converts feet and inches to centimeters.")
feet=input("Enter number of feet: ")
inches=input("Enter number of inches: ")
feet_to_inches=int(feet) * 12
feet_to_inches1=int(feet_to_inches) + int(inches)
centi=float(feet_to_inches1)*2.54
print("{} ft {} in = {} cm".format(feet,inches,centi))
