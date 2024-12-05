"""
Author: Paul Sommers
Date written: 12/5/2024
Assignment: Module 07 Programming Assignment 2
Short Desc: This program defines an Employee class and a ProductionWorker subclass. It creates an instance of ProductionWorker, 
            prompts the user for input, and displays the stored information using accessor methods.
"""

# Define the Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Accessor (getter) methods
    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    # Mutator (setter) methods
    def setName(self, name):
        self.__name = name

    def setNumber(self, number):
        self.__number = number

# Define the ProductionWorker class, a subclass of Employee
class ProductionWorker(Employee):
    def __init__(self, name, number, payRate, shift):
        # Call the superclass (Employee) constructor
        super().__init__(name, number)
        self.__payRate = payRate
        self.__shift = shift

    # Accessor (getter) methods
    def getPayRate(self):
        return self.__payRate

    def getShift(self):
        return self.__shift

    # Mutator (setter) methods
    def setPayRate(self, payRate):
        self.__payRate = payRate

    def setShift(self, shift):
        self.__shift = shift

# Main program
def main():
    # Prompt the user for ProductionWorker details
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    payRate = float(input("Enter hourly pay: "))
    shift = int(input("Enter shift number (1 for day, 2 for night): "))

    # Create a ProductionWorker
    worker = ProductionWorker(name, number, payRate, shift)

    # Display the details
    print("\nEmployee Details:")
    print(f"Name: {worker.getName()}")
    print(f"Employee Number: {worker.getNumber()}")
    print(f"Hourly Pay Rate: ${worker.getPayRate():.2f}")
    print(f"Shift: {'Day' if worker.getShift() == 1 else 'Night'}")

# Run the program
main()