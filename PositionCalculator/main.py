""""
To prevent being stuck in an unfavorable position, it is important 
to manage your account to minimize losses and take the most optimial moves posissible.
"""
"""
0: the number of the total account
1: a dictionary object with the following items
a: amount used for swing trading 
b: amount used for day trading 
aa: amount used for calls
ab: amount used for puts
aaa && aba: daily maximum limit for opening a new position
"""
percentage = lambda x,p : x*(p*0.01)
def position (n):
    data = dict({"total account": 0, "swing trade": 0, "day trade": 0, "amount for calls": 0, "amount for puts": 0, "daily call position": 0, "daily put position": 0,"Optimal Buying power":0,})

    data["total account"] = n
    data["swing trade"] = percentage(n,80)
    data["day trade"] = percentage(n,20)
    data["amount for calls"] = percentage(data["swing trade"],50)
    data["amount for puts"] = percentage(data["swing trade"],50)
    data["daily call position"] = percentage(data["amount for calls"],50)
    data["daily put position"] = percentage(data["amount for puts"], 50)
    data["Optimal Buying power"] = data["day trade"] + data["daily call position"] + data["daily put position"]

    return data

def printposition(pos):
    for x in pos:
        print("{} : {}".format(x, pos[x]))


#print(position(10000))
printposition(position(9968.44))