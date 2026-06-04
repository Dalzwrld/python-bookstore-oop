title = input("Enter the title of the book: ")
page_count = int(input("Enter the page count of the book: "))

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        Book.page_count += 1

    @page_count.setter
    def page_count(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")