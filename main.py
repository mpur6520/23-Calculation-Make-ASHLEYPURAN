#Maru Puran
#September 28, 2023
#code with variables, integers, and expressions in order to gain a better understanding of how arithmetic works when programming as well as a better idea of what can be done with it


# Program to calculate the area of a rectangle

print("\nHello! Let's calculate the perimeter and area of a rectangle. :)\n")

# Get input for height & width. Convert to integers and store in variables

height = int(input("Please enter a height for your rectangle: "))
width = int(input("Please enter a width for your rectangle: "))

# Calculate the area + perimeter & store the result in the area variable

area = height*width
perimeter = height*2 + width*2


# Output the area and perimeter variable (converted to string)

print("\nThe area of your rectangle is " + str(area) + "!")
print("The perimeter of your rectangle is " + str(perimeter) + "!")

# -------------------------------------

# Program to calculate a resturaunt tip 

print("\n\nHello! Let's calculate a resturaunt tip.")

# get input for the price of the meal and store in a variable

price = int(input("Please enter the price of your meal here: "))

#Calculate the amount of tip at 20%, total price, & store into a variables

tip = price*0.20
total_price =  price*1.20

# Output the tip and total price variables converted to strings

print("\nYour tip will be " + str(tip) + ", and your total price will be " + str(total_price) + "!")

# -------------------------------------

# Program to calculate a volume + total surface area of a cuboid

print("\n\nHello! Let's calculate the volume and total surface area of a cuboid!\n")

# get input for the height, width, length, convert to integers and store it into a variable

height_cuboid = int(input("Please enter a height: "))
width_cuboid = int(input("Please enter a width: "))
length_cuboid = int(input("Please enter a length: "))

# calculate the volume and total surface area of the cuboid, store into variables

total_surface_area = 2*(length_cuboid*width_cuboid) + 2*(length_cuboid*height_cuboid) + 2*(width_cuboid*height_cuboid)
volume = length_cuboid*width_cuboid*height_cuboid

# output the total surface area and volume variables converted to strings

print("\nThe volume of your cuboid is " + str(volume) +"!")
print("The total surface area of your cuboid is " + str(total_surface_area) + "!")