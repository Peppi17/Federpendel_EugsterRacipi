# Zeitangabe oben rechts

from round import round1

def timer(posX, posY, t, text_size):
    
    
    fill(0)
    textAlign(LEFT, TOP)
    text("Zeit:  ", posX-11*text_size, posY+15)
    textAlign(RIGHT, TOP)
    text(str(round1(t)) + " Sekunden", posX-20, posY+15)
