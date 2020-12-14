# Erstellt einen Knopf abhaengig von Position, Laenge, Breite, Farbe, Konturfarbe, Konturdicke, Beschriftung und Textgroesse

def button(kontur_dicke, kontur_farbe, button_farbe_r, button_farbe_g, button_farbe_b , button_xpos, button_ypos, button_laenge, button_breite, name, text_size):
    
    noStroke()
    fill(50)
    rect(button_xpos+4, button_ypos+4, button_laenge, button_breite)

    strokeWeight(kontur_dicke)
    stroke(kontur_farbe, kontur_farbe, 0)
    fill(button_farbe_r, button_farbe_g, button_farbe_b)
    rect(button_xpos, button_ypos, button_laenge, button_breite)
    textAlign(CENTER)
    fill(255)
    textSize(text_size)
    text(name, button_xpos + button_laenge/2 , button_ypos + 2*button_breite/3)
