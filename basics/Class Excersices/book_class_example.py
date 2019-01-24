class Book:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def incerase_copies(self,number_of_copies):
        print(' Increasing copies by :', number_of_copies)
        self.copies += number_of_copies

    def decerase_copies(self,number_of_copies):
        print(' Decreasing copies by :', number_of_copies)
        self.copies -= number_of_copies


python_book = Book('Intro to Python', 3)

print(python_book.name, 'Number of Copies:', python_book.copies)

python_book.incerase_copies(4)

print(python_book.name, 'Number of Copies:', python_book.copies)

python_book.decerase_copies(4)

print(python_book.name, 'Number of Copies:', python_book.copies)
