class mononial:

    def __init__(self,a,x='x',d=1):
        self.a = a
        self.x = x
        self.d = d

    def __str__(self):
        if self.d !=1:
            return " {}{}^{}".format(self.a,self.x,self.d)
        else:
            return " {}{}".format(self.a, self.x)

    def __add__(self, rhs):
        if self.x == rhs.x and self.d == rhs.d:
            newa = self.a + rhs.a 
            #z = mononial(newa, self.x, self.d)
            #print("{} + {} = {}".format(self.__str__(), rhs.__str__(),z.__str__()))
            return mononial(newa, self.x, self.d)
        return self

      
class equation:
    def __init__(self, *args):
        self.args = [*args]

    def __str__(self):
        #return [i if ]
        posorNeg = lambda x : "+{}".format(x) if x.a>=0 else "-{}".format(x)
        lis = list(map(posorNeg, self.args))
        return ("{}"*len(lis)).format(*lis)

    def printt(self):
        print(self.args)




a = mononial(1)
b = mononial(2,d="2")
c = mononial(7)
g = mononial(-6)
# print(a+b+c)
d = equation(a,b,c,g)
print(d)
