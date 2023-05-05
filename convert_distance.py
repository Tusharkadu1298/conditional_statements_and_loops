# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

distance_feet = float(input("enter the distance in feet :-- "))
distance_inches = distance_feet * 12
distance_yards = distance_feet / 3.0
distance_miles = distance_feet / 5280.0 
print()
print("-"*50)
print("The distance in inches is :-- ", distance_inches)
print("The distance in yards is :--  ", distance_yards)
print("The distance in miles is :-- ", distance_miles)
print("-"*50)
