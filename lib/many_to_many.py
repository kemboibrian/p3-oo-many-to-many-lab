class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Invalid title")
        self.title = title
        self.authors_list = []
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))

    def __str__(self):
        return f"{self.title}"

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Invalid name")
        self.name = name
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
