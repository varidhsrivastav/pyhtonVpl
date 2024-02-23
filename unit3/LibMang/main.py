from Book import  Book
# from Transaction import  Transaction
from Liberary import   Library
from Customer import     Customer
library1 = Library("Central Library", "123 Main St")
library2 = Library("Community Library", "456 Elm St")
Customer1=Customer("Minesh","srivari enclave")
book1 = Book("Python Programming", "John Doe", 10)
book2 = Book("Data Science Handbook", "Alice Smith", 5)
book3 = Book("Machine Learning Basics", "John Doe", 8)
book4 = Book("Introduction to Statistics", "Bob Johnson", 6)

library1.add_book(book1)
library1.add_book(book2)
library2.add_book(book3)
library2.add_book(book4)

print("Total books in Library 1:", library1.get_total_books())
print("Total books in Library 2:", library2.get_total_books())

