# Zeitangabe oben rechts

def timer(posX, posY, t, text_size):
    fill(0)
    textAlign(LEFT, TOP)
    text("Zeit:  ", posX-10.5*text_size, posY+15)
    textAlign(RIGHT, TOP)
    text(str(int(t)) + " Sekunden", posX-20, posY+15)
