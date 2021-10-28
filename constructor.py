class Apple:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, color, weight, taste):
        self.color = color
        self.weight = weight
        self.taste = taste

jonagold = Apple("red", 100, "sweet")
print(jonagold.color)