class Coffee:
    SIZE = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in Coffee.SIZE:
            raise ValueError(f"Size must be {Coffee.SIZE[0]}, {Coffee.SIZE[1]}, or {Coffee.SIZE[2]}")
        
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1
    
print(Coffee.__dict__)