class Book:
    _all_books = []  

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book._all_books.append(self)

    @classmethod
    def all_books(cls):
        
        return cls._all_books

    def __str__(self):
        return f"Book: {self.title}"


class Author:
    _all_authors = []  

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        Author._all_authors.append(self)  

    @classmethod
    def all_authors(cls):
        
        return cls._all_authors

    def contracts(self):
        
        return [contract for contract in Contract.all_contracts() if contract.author == self]

    def books(self):
        
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book: Book, date: str, royalties: int):
        
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        if royalties < 0 or royalties > 100:
            raise Exception("Royalties must be between 0 and 100.")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Returns the total royalties from all contracts the author has signed."""
        return sum(contract.royalties for contract in self.contracts())

    def __str__(self):
        return f"Author: {self.name}"


class Contract:
    _all_contracts = []  

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        
        
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        if royalties < 0 or royalties > 10000:
            raise Exception("Royalties must be between 0 and 100.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all_contracts.append(self)  

    @classmethod
    def all_contracts(cls):
        
        return cls._all_contracts

    @classmethod
    def contracts_by_date(cls, date: str):
        
        return [contract for contract in cls._all_contracts if contract.date == date]

    def __str__(self):
        return (f"Contract Details:\n"
                f"Author: {self.author.name}\n"
                f"Book: {self.book.title}\n"
                f"Date: {self.date}\n"
                f"Royalties: {self.royalties}%")
