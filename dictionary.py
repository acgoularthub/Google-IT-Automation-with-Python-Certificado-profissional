#In Python, a dictionary can only hold a single value for a given key. 
# To workaround this, our single value can be a list containing multiple values. 
# Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
# Fill in the blanks to print a line for each item of clothing with each color, 
# for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
#the commented code will print the same thing as the code below
#result = [clothes + " " + color for color in wardrobe for clothes in wardrobe[color]] 
result = []
for color in wardrobe:
	for clothes in wardrobe[color]:
		result.append(clothes + ' ' + color)

for strings in result:
	print(strings)