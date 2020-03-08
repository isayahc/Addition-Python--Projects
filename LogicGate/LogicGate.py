class LogicGate:

    def __init__(self, n):
        self.label = n 
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None 

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate" + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + self.getLabel()+"-->"))
        else: 
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """the connector must be connected to one line.
        if both of them are available, we will choose pinA by default. If pinB
        is already connected, then we will choose pinB. It is not possible to conect
        to a gate with no available input lines"""
        if self.pinA == None:
            self.pinA = source 
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate" + self.getLabel()+"-->"))

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")



"""Notes
- self is a reference to the object itself
- get logic gate had one or two input lines
 - binarygates have 2 input lines
 - unary has 2 input 

-The constructors in both classes start with an explicit call
to the constructor of the parent class using the parent's __init__

SUPER can be used to in place of explicitly namein the parent class. Especially 
when the class has more than one parent.

ex:
LogicGate.__init__(self,n) could be replaced super(UnaryGate, self).__init__(n)


"""

"""AndGate will be a subclass of binarygate becuase it has two outputs.

"""

class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a and b ==1 else 0


class OrGate(BinaryGate):

    def __init__(self,n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a or b ==1 else  0
        # if a or b ==1: return 1
        # else: return 0 

class NotGate(UnaryGate):
    
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        return 0 if self.getPin() else 1


'''
A connector connects gates together
- will not be in the gate heirarchy
 - it will use the heirarchy in that wach connector will have to gates
 - called the "HAS-A relationship"
  - does not require Inheritance
 - Ex: UnaryGate "IS-A" LogicGate
  - requires inheritance



'''

class Connector:

    def __doc__(self):
        """
        -to represent flow 
        - it will need a togate 
        - it will need a fromfate
         """

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate 

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate



def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
