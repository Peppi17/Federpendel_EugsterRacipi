


# Zeitangabe oben rechts
def timer(posX, posY, t, text_size):
    fill(0)
    textAlign(LEFT, TOP)
    text("Zeit: " + str(int(t)), posX-11.5*text_size, posY+20)
    textAlign(RIGHT, TOP)
    text( "Sekunden", posX-20, posY+20)
