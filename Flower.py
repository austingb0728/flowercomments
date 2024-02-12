# Name: Austin Kennedy
# Date: February 11th, 2024
# Description: This code defines a class called Flower with attributes for the name of the flower.


class Flower:
    def __init__(self, name):  # Constructor method with attribute: name
        self.name = name  # Assigning name attribute


    def grow(self):  # Method to simulate growth of the flower
        print("The " + self.name + " is growing.")  # Printing a message indicating growth


    def bloom(self):  # Method to simulate blooming of the flower
        print("The " + self.name + " is blooming.")  # Printing a message indicating blooming


def main():  # Main function to demonstrate the Flower class
    flower1 = Flower("Rose")  # Creating a Flower class called "flower1" with name attribute "Rose"
    flower1.grow()  # Calling the grow method for "flower1"
    flower1.bloom()  # Calling the bloom method for "flower1"
    flower2 = Flower("Daisy")  # Creating another Flower class called "flower2" with name attribute "Daisy"
    flower2.grow()  # Calling the grow method for "flower2"
    flower2.bloom()  # Calling the bloom method for "flower2"


if __name__ == "__main__":  # Checking if the script is being run as the main program
    main()  # Calling to execute the code