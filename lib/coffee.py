size = input("Enter the size of the coffee: ")
price = float(input("Enter the price of the coffee: "))

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price