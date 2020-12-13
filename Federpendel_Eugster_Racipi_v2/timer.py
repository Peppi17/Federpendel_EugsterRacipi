


# Zeitangabe oben rechts
def timer(posX, posY, t, text_size):
    fill(0)
    textSize(text_size)
    textAlign(RIGHT)
    text("Zeit: " + str(t) + " Sekunden", posX, posY)
