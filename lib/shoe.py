# Create a Shoe class in shoe.py
class Shoe:
    # Constructor method (__init__) initializes the instance with brand and size
    def __init__(self, brand, size):
        # Check if size is an integer, otherwise print an error message
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self.brand = brand
            self.size = size

    # Method to indicate that the shoe has been repaired
    def repair_shoe(self):
        print("The shoe has been repaired.")
        # Create an attribute 'condition' and set it to 'New' after repair
        self.condition = 'New'
        