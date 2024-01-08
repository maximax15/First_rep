# task1
class CardDeck:
    def __init__(self):
        self.index = 0
        self.length = 52
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']
    def __iter__(self):
        return self
    def __next__(self):
        for i in range(0, len(self.__SUITS)):
            for j in range(0, len(self.__RANKS)):
                print(f'{self.__RANKS[j]} {self.__SUITS[i]}')
                self.index += 1
                if self.index >= self.length:
                    raise StopIteration

koloda = CardDeck()

for el in koloda:
    print(el)

# task2
def fib(n):
    num1, num2 = 0, 1
    for i in range(0, n):
        num1, num2 = num2, num1 + num2
        yield num1

print(list(fib(3)))






