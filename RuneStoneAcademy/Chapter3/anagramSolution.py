""""
Goal: Write an boolean function that will 2 strings and 
see if they are anagrams
"""

from timeit import Timer
from collections import Counter

def anagramSolution1(s1,s2):

    stillOK = True
    if len(s1) != len(s2):
        stillOK = False
    
    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        
        pos1 = pos1 + 1
        
        
    return stillOK

# print(anagramSolution1('abcd','dcba'))
# print(anagramSolution1('aabcd','aadcb'))

def test1():
    anagramSolution1('aabcd','aadcb')
def test2():
    StringToDict2("hello") == StringToDict2("helol")


def StringToDict(string):
    dictword = dict()
    for i in string:
        if i in dictword:
            dictword[i] += 1
        else:
            dictword.update({i:1})

    return dictword

def StringToDict2(string):
    counts = dict()
    for i in string:
        counts[i] = counts.get(i, 0) + 1

    return counts

print(StringToDict2("hello") == StringToDict2("helol"))

Compare = lambda s1,s2 : s1 == s2



# k = StringToDict("dude")
# b = StringToDict("deud")
# print(k==b)


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("concat ",t2.timeit(number=1), "milliseconds")

print(test2())
