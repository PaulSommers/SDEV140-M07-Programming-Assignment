"""
Author: Paul Sommers
Date written: 12/5/2024
Assignment: Module 07 Programming Assignment 1
Short Desc: This program defines a Person class and a Customer subclass. It demonstrates the use of the Customer class by creating an instance and displaying its attributes.
"""

# Define the Person class
class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

# Define the Customer class, a subclass of Person
class Customer(Person):
    def __init__(self, name, address, telephone, customerNumber, mailingList):
        # Call the superclass 
        super().__init__(name, address, telephone)
        self.customerNumber = customerNumber
        self.mailingList = mailingList

# Example customer class
def main():
    # Create an instance of the Customer class
    customer = Customer(
        name="John Doe",
        address="123 Main St, Anytown, USA",
        telephone="555-1234",
        customerNumber=1001,
        mailingList=True
    )

    # Display the customer's details
    print("Customer Details:")
    print(f"Name: {customer.name}")
    print(f"Address: {customer.address}")
    print(f"Telephone: {customer.telephone}")
    print(f"Customer Number: {customer.customerNumber}")
    print(f"On Mailing List: {'Yes' if customer.mailingList else 'No'}")

# Run the program
main()