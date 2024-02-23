class Transactions:
    def __init__(self, name):
        self.name = name
        self.books=[]
        self.borrowed=True
    def borrowBook(self, book):
        self.books.append(book)
        
    def isBorrowed(self):
        return self.borrowed
    def returned(self):
        self.borrowed=False
        return self.borrowed
    



    # create a package called as calculator the first module sould contain mathematical and srithmatic calculation second should contain scientific calculation
    # third module contain area calculation
    # creaete a menu  for user to select the type of operation he want to perform