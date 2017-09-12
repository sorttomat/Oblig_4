
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
        elif (a == 1 and b != 1) or (b == 1 and a != 1):
            Cout = 1
            S = 0
        else:
            Cout = 0
            S = 1
    elif Cin == 0:
        S, Cout = halvadder(a, b)
    return S, Cout



def multiplikator1010(bin3, bin2, bin1, bin0):
    Sum1, Cout1 = halvadder(bin2, bin0)
    Sum2, Cout2 = adder3Input(bin3, bin1, Cout1)
    Sum3, Cout3 = halvadder(Cout2, bin2)
    Sum4, Cout4 = halvadder(Cout3, bin3)
    resultat = [Cout4, Sum4, Sum3, Sum2, Sum1, bin1, bin0, 0]
    return resultat


resultat = multiplikator1010(1, 1, 1, 1)
print(resultat)
    
            
        
    


