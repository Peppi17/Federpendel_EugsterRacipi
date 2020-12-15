# Auslenkung Echtzeit oben rechts

from round import round1

def auslenkung(posX, posY, t, text_groesse, A, omega):
    
    fill(0)
    textAlign(LEFT, TOP)
    text("Auslenkung:  ", posX-11*text_groesse, posY+15+text_groesse+5)
    textAlign(RIGHT, TOP)
    text(str(round1(A*cos(omega * t)*10)) + " cm", posX-20, posY+15+text_groesse+5)
