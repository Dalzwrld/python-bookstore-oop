title = input("Enter the title of the book: ")
page_count = int(input("Enter the page count of the book: "))

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        Book.page_count += 1
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")