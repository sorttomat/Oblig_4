
def halvadder(a, b):
    if a == 1 and b == 1:
        Cout = 1
        S = 0
    elif (a == 1 and b != 1) or (b == 1 and a != 1):
        Cout = 0
        S = 1 
    else:
        Cout = 0
        S = 0   
    return S, Cout


def adder3Input(a, b, Cin):
    if Cin == 1:
        if a == 1 and b == 1:
            Cout = 1
            S = 1
            return S, Cout
        elif (a == 1 and b != 1) or (b == 1 and a != 1):
            Cout = 1
            S = 0
            return S, Cout
        else:
            Cout = 0
            S = 1
            return S, Cout
    elif Cin == 0:
        if a == 1 and b == 1:
            Cout = 1
            S = 0
            return S, Cout
            
        elif (a == 1 and b != 1) or (b == 1 and a != 1):
            Cout = 0
            S = 1
            return S, Cout
        else:
            Cout = 0
            S = 0
            return S, Cout



def multiplikator1010(bin3, bin2, bin1, bin0):
    Sum1, Cout1 = halvadder(bin2, bin0)
    print(Sum1, Cout1)
    Sum2, Cout2 = adder3Input(bin3, bin1, Cout1)
    print(Sum2, Cout2)
    Sum3, Cout3 = halvadder(Cout2, bin2)
    print(Sum3, Cout3)
    Sum4, Cout4 = halvadder(Cout3, bin3)
    print(Sum4, Cout4)
    resultat = [Cout4, Sum4, Sum3, Sum2, Sum1, bin1, bin0, 0]
    return resultat

resultat = multiplikator1010(1, 0, 1, 0)
print(resultat)
    
            
        
    


