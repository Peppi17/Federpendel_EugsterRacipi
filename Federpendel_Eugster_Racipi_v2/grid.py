


def grid(xscl, yscl, xmax, xmin, ymax, ymin, text_size):
    background(255) # weisser Hintergrund

    for i in range(0, (xmax-xmin)/xscl): # Senkrechte Linien
        strokeWeight(1)
        stroke(220)
        line(i*xscl, ymax, i*xscl, ymin)

    for i in range(0, (ymax-ymin)/yscl): # Waagrechte Linien
        strokeWeight(1)
        stroke(220)
        line(xmin, i*yscl, xmax, i*yscl) # Zwei Linien gespiegelt an der X-Achse
        line(xmin, -i*yscl, xmax, -i*yscl)
    
    strokeWeight(2)
    stroke(0)
    line(xmin, 0, xmax, 0) # X-Achse
    line(xmin, ymin, xmin, ymax) # Y-Achse
    fill(0)
    triangle(xmax,0,xmax-5,5,xmax-5,-5) # Spitze X-Achse
    triangle(0,ymin,-5,ymin+5,5,ymin+5) # Spitze  Y-Achse
    textSize(text_size)
    textAlign(LEFT, TOP)
    text("Amplitude A", 20,ymin+20) # Text "Amplitude A" zur Y-Achse
    textAlign(RIGHT, TOP)
    text("Zeit t",xmax-20, 20) # Text "Zeit t" zur X-Achse
    
