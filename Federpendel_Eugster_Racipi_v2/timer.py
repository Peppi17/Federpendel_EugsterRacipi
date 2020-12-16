# Zeitangabe oben rechts

from round import round1

def timer(posX, posY, t, text_groesse):
    
    fill(0)
    textAlign(LEFT, TOP)
    text("Zeit:  ", posX-12*text_groesse, posY+15)
    textAlign(RIGHT, TOP)
    text(str(round1(t)) + " Sekunden", posX-20, posY+15)
