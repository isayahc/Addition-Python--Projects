from pythonds.basic import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEFG"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base 

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString

print(baseConverter(25,2))
print(baseConverter(250,16))  