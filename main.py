def nand(n1,n2):
    return not (n1 and n2)

def nor(n1,n2):
    return not (n1 or n2)

def hnand(n1,n2,mode=0): #my original
    if mode == 0:
        return (not n1) and n2
    else:
        return n1 and (not n2)

def xor(n1,n2):
    return hnand(n1,n2,1) or hnand(n2,n1,1)

def hnxor(n1,n2,mode=0): #my original
    if mode == 0:
        return xor(not n1,n2)
    else:
        return xor(n1,not n2)

def xnor(n1,n2):
    return not xor(n1,n2)

def