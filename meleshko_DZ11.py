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
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []
    def deposite(self, amount):
        self.__balance += amount
        self.__transactions.append(f'добавлена {amount} на твой счет')
    def withdraw(self, amount):
        self.__balance -= amount
        self.__transactions.append(f'вычтено {amount} с твоего счета')
    def add_interests(self):
        self.__balance = self.__balance + self.__balance * (self.__interest_rate / 100)
        self.__transactions.append(f'добавлено  {self.__balance * (self.__interest_rate/100)}(сумма с процента) на твой счет')
    def history(self):
        print(self.__transactions)

account = BankAccount(1500, 20)

account.add_interests()
print(account._BankAccount__balance)
account.deposite(1500)
account.withdraw(100)
print(account._BankAccount__balance)
account.history()
print(account._BankAccount__balance)