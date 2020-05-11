'''
input: String ex "Ax^2"
find A
take vars 
output: 
'''
from pythonds.basic import Stack


class Term:
    def __init__(self, x, a=1, n=1):
        self.a = a
        self.x = x
        self.n = n
    def __str__(self):
        if self.n == 1:
            return "{}{}".format(self.a, self.x)
        else: 
            return "{}{}^{}".format(self.a, self.x, self.n)

    def __add__(self, rhs):
        if (self.x == rhs.x) and (self.n == rhs.n):
            newa = self.a + rhs.a
            return Term(self.x,newa,self.n)
        else:
            return None
    def __mul__(self, rhs):
        if type(rhs) == int:
            return Term(self.x, self.a*rhs,self.n)
        elif type(rhs) == Term:
            Term(self.x+rhs.x,self.a*rhs.a, self.n+rhs.n) if self.x != rhs.x else  0


class polynomial:
    #check for balance paranthesis 
    #simplify 
    def __init__(self, string):
        self.data = string

    def __str__(self):
        return self.data

# class polynomial:
#     def __init__(self, string):
#         #number of time to search 
#         lis = list(string)
#         # for list(string).count("^") in string:
#         # if "^" in string:
#         #     print(lis.index

# def func1(string):
#     """enter string with parenthesis
#     return dict with begining, middle, end
#     """
#     for i in string:
#         if i == "(":
#             prior = string[0: string.find('(')]
#             if ')' not in string:
#                 raise RuntimeError
#             middle = string[string.find('(')+1: string.find(')')]
#             if



# x = "x(2x)"

# func1(x)

# def func2(string):
#     counter =0
#     for i in string:
#         print(i)
#         if i = "(":
#             while i not ')':
#                 counter += 1

# def test(t):
#     if t != '':
#         print(t)
#         return test(t[:-1])

# def attempt(t):
#     l = [*test('cat')]
#     print(l)




# test("cat")
# attempt("cat")

'''
Enter String:
if '(' in string
'''

# def inner(x):
#     count = 0
#     start = 0
#     end = 0
#     for i in x:
#         if i == '(':
#             print(x[count])
#             start = count
            
#         if i == ')':
#             print(x[count])
#             end = count
#         count +=1
#     print(x[start:end])

# inner("2x(3x(10))")

# x ="2x(3x(10))"
# print(x.split("("))
# t = Term("c",5)
# k = Term("d",5,5)
# d = Term("c",5)
# print(t)
# print(k)
# print(d)
# print("{}*{} = {}".format(t,k,t*k))
# print("{}*{}*{} = {}".format(t,k,d,t*k*d))
# ##if multi then multply


# x = {"x":2, 'y':3}
# a = 10

# x.items()
# x.get

# print(x.__len__())
# #prints 2 for x

# def printt (a,x):
#      return '{}'.format(a) + str(('{}^{}'*x.__len__()).format([*x.items()]))

# print(printt(a,x))

# def test(a,x):
#     q = a
#     e = [*x.items()][0]
#     r = [*x.items()]
#     print("test")
#     #print([*r, r.__len__()])
#     t = [ a,b for i in r]
#     return "{}".format(a) + "{}^{}".format(*e)

# print(test(1,{'a':4,'b':7}))

# c = {'a':4,'b':7}
# print(type(c))

# for i in c:
#     print(*([i,c[i]]))

# k = [([i,c[i]]) for i in c][0]
# for i in k:
#     print("{}^{}".format((*(i))))

def add(a,b):
    return a,b

a = {'S':3,'D':7}


def printout(a,x):
    ni = str()
    for i in x:
        ni += "{}^{}".format(i,x[i])
    return "{}{}".format(a,ni)

print(printout(12,a))