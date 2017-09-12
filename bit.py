multiplikator = [1, 0, 1, 0]

def halvadder(a, b):
    Cout = 0
    S = 0
    if a == 1 and b == 1:
        Cout = 1
        S = 0
    elif (a == 1 and not b == 1) or (b == 1 and not a == 1):
        Cout = 0
        S = 1
    
    return S, Cout

def adder2(a, b, Cin):
    Cout = 0
    S = 0
    

