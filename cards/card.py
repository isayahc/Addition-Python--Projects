class Card:

    def __init__(self, rank, suite):
        """ Important: 
        <rank><Suit> """
        self.suite = suite 
        self.rank = rank
    
    def __eq__ (self, newcard):
        return self.getRank() == newcard.getRank()

    def __add__(self, newcard):
        return self.getRank() + newcard.getRank()

    def __str__(self):
        return str("{}|{}".format(self.rank, self.suite))

    def __repr__(self):
        pass
        
    def getSuite(self):
        return self.suite
    
    def getRank(self):
        additionranks = list('TJQKA')
        if self.rank not in additionranks:
            return self.rank
        d = {suite: rank for rank,suite in enumerate(additionranks,10)}
        return d[self.rank]


class Hand:
    def __init__(self, cardA,cardB,cardC):
        self.cardA = cardA
        self.cardB = cardB
        self.cardC = cardC

    def __str__(self):
        return "{} {} {}".format(self.cardA, self.cardB, self.cardC)

    def allSuites(self):
        return [self.cardA.getSuite(), self.cardB.getSuite(), self.cardC.getSuite() ]

    def allRanks(self):
            return [self.cardA.getRank(), self.cardB.getRank(), self.cardC.getRank() ]

    def allCard(self):
        return [self.cardA, self.cardB, self.cardC]

    def ValidRun(self):
        """adjust for Ace"""
        return (self.cardA.getRank() + self.cardB.getRank() + self.cardC.getRank())%3 ==0

    def ThreeofKind(self):
        return self.cardA.getSuite() ==self.cardB.getSuite() == self.cardC.getSuite()
    
    def Flush(self):
        return self.cardA.getSuite() == self.cardB.getSuite() == self.cardC.getSuite()

    def StraightFlush(self):
        return self.ValidRun() and self.Flush

    def Pair(self):
        return (all(self.allRanks == self.allRanks()[0]))

    def HighCArd(self):
        return not (self.ThreeofKind or self.Flush or self.Pair)

    

class Game:
    def __init__(self, players, *hands):
        self.player = players 
        self.hands = hands

    

x = Card(2, "C")
y = Card('A', "H")
z = Card(4, "D")
a = Hand(x,y,z)
m = Card('A', "H")
n= Card('A', "H")
v= Card('A', "H")
c = Hand(m,n,v)
print(c.ThreeofKind())
print(y.getRank())
print(a)
print(x==y)
print(a.ThreeofKind())
print(a.ValidRun())
