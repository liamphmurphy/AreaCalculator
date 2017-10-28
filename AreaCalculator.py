print("Welcome to the Area Calculator!")

print("Here are a list of shapes you can calculate the area for. Type 1, 2, 3 etc!")

# \n's for list
print("1. Triangle\n2. Square\n3. Cylinder\n4. Circle")

# get user choice
userChoice = int(input())

# triangle
if userChoice == 1:
	print("You have chosen a triangle, which is half of the base times the height.")

	triB = int(input("First, type the base of the triangle: "))
	triH = int(input("Now type the height of the triangle: "))
	triCalc = triB * triH * 1/2
	triCalc = str(triCalc)
	print("The answer is: " + triCalc)

# square
elif userChoice == 2:
	print("You have chosen a square, which is simply width times height, or a^2.")
	squareA = int(input("Type in the width or height, because it's a square, it's the same number: "))
	squareCalc = squareA * squareA
	squareCalc = str(squareCalc)
	print("The answer is: " + squareCalc)

# cylinder
if userChoice == 3:
	print("You have chosen a cylinder, which is a more complicated equation.")

	cylR = int(input("First, type the radius of the cylinder: "))
	cylH = int(input("Now type the height of the cylinder: "))
	cylCalc = ((2*3.14) * (cylR*cylH)) + ((2*3.14) * (cylR*cylR))
	cylCalc = str(cylCalc)
	print("The answer is: " + cylCalc)

# circle
if userChoice == 4:
	print("You have chosen a circle, which is pi (3.14) times radius squared.")

	circR = int(input("Type the radius of the circle: "))
	circCalc = 3.14 * (circR*circR)
	circCalc = str(circCalc)
	print("The answer is: " + circCalc)