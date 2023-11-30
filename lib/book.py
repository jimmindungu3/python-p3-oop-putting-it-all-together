class Book:
    # Constructor method (__init__) initializes the instance with title and page_count
    def __init__(self, title, page_count):
        # Check if page_count is an integer, otherwise print an error message
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self.title = title
            self.page_count = page_count

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        