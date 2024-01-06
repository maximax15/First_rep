# task1
class Publication():
    publisher = 'слепой крот'
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def dispaly(self):
        print(self.title)
        print(self.author)
        print(self.year)
    @classmethod
    def get_publisher(Publication):
        print(Publication.publisher)

class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn
    def dispaly(self):
        print(super().dispaly())
        print(self.isbn)
class Magazine(Publication):
    def __init__(self,title, author, year, issue_number ):
        super().__init__(title, author, year)
        self.issue_number = issue_number
    def dispaly(self):
        print(super().dispaly())
        print(self.issue_number)
book1 = Book('Kat', 'Labkowski', 2011, '1231')
book1.dispaly()
magazine1 = Magazine('dog', 'S.Sheldon', 1990, 25)
magazine1.dispaly()
book1.get_publisher()
# task2
class BankAccount():
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
    def deposite(self, amount):
        self.balance += amount
        self.transactions.append(f'добавлена {amount} на твой счет')
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'вычтено {amount} с твоего счета')
    def add_interests(self):
        self.balance = self.balance + self.balance * (self.interest_rate / 100)
        self.transactions.append(f'добавлено  {self.balance * (self.interest_rate/100)}(сумма с процента) на твой счет')
    def history(self):
        print(self.transactions)
account = BankAccount(1000, 2)
account.deposite(500)
account.withdraw(200)
account.add_interests()
account.history()
print(account.balance)