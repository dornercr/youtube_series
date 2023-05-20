# Define a class called Car
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The {self.color} {self.brand} is starting the engine.")

# Create a Car object with brand "Tesla" and color "red"
my_car = Car("Tesla", "red")

# Create another Car object with brand "Porsche" and color "yellow"
my_car2 = Car("Porsche", "yellow")

# Call the start_engine method on the my_car object
my_car.start_engine()

# Call the start_engine method on the my_car2 object
my_car2.start_engine()

"""
    -The Car class is defined, which has an __init__ method and a start_engine method.
    -The __init__ method is the constructor that initializes the brand and color attributes of a Car object.
    -The start_engine method is a function that prints a message indicating the car's color and brand.
    -An instance of the Car class is created and assigned to the my_car variable with the brand "Tesla" and 
    color "red".
    -Another instance of the Car class is created and assigned to the my_car2 variable with the brand "Porsche" and 
    color "yellow".
    -The start_engine method is called on the my_car object, which prints the message indicating that the red Tesla is 
    starting the engine.
    -The start_engine method is called on the my_car2 object, which prints the message indicating that the yellow Porsche 
    is starting the engine.
"""