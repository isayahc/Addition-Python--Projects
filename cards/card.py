class Card:

    def __init__(self, suite, rank):
        self.suite = suite 
        self.rank = rank
    
    def __eq__ (self, newcard):
        print(self.suite, newcard.suite)
        return self.suite == newcard.suite

    def __add__(self, newcard):
        return self.rank + newcard.rank

    def __str__(self):
        return str("{}|{}".format(self.suite, self.rank))

    def ValidRun(self):
        return 0
    #isFlush = lambda *x : sum(x)/(x.sort()[2]) == 3

class Hand:
    def __init__(self, cardA,cardB,cardC):
        self.cardA = cardA
        self.cardB = cardB
        self.cardC = cardC

    def __str__(self):
        return "{} {} {}".format(self.cardA, self.cardB, self.cardC)

    

x = Card('A',1)
y = Card('A',5)
z = Card('B',6)
a = Hand(x,y,z)
print(a)

