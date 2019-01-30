class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return ('Review Id: ' + str(self.id)
              + '  Description: ' + self.description
              + '  Rating: ' + str(self.rating))


class Book:
    def __init__(self, name, id, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        rev = '\n'
        for single_review in self.reviews:
            rev += single_review.__repr__()
            rev += '\n'
        return ('Book id: ' + str(self.id)
              + '\nBook Name: ' + self.name
              + '\nBook Author: ' + self.author
              + '\nBook Reviews:'  + rev)

book1 = Book('Naruto', 700, 'Masashi Kishimoto')
# print(book1)
# print(review)
book1.add_review(Review(1, 'Number 1 Knuckleheaded Hero', 5))
book1.add_review(Review(2, 'Konoha no Eiyuu', 5))
print(book1)