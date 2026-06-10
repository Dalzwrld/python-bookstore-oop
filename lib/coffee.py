size = input("Enter the size of the coffee (Small, Medium, Large): ")
price = float(input("Enter the price of the coffee: "))

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            raise ValueError("size must be 'Small', 'Medium', or 'Large'")
        
    def tip(self, price):
        print("This coffee is great, here's a tip!")
        price += 1
        return price
    
print(Coffee.__dict__)