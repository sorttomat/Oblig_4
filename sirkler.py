"""
Dette programmet tegner opp 9 sirkler paa et lerret i et vindu, der sirklene baade forflytter seg og endrer
stoerrelse.
"""
from ezgraphics import GraphicsWindow

win = GraphicsWindow(500, 500)
can = win.canvas()

#Definerer startverdiene
teller = 0
x_pos = 10
stoerrelse = 50

#While-loekken kjorer saalenge teller er mindre enn 9, dvs 9 ganger (0-8).
#Hver gang tegnes det opp en ny sirkel.
while teller < 9:
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    #Oeker verdiene:
    x_pos += 10
    teller += 1
    stoerrelse += 5

win.wait()

