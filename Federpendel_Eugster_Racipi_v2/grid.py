# Erstellt das Raster

def grid(xscl, yscl, xmax, xmin, ymax, ymin, text_groesse):
        
    # weisser Hintergrund
    background(255) 

    # Senkrechte Linien
    for i in range(0, (xmax-xmin)/xscl):
        strokeWeight(1)
        stroke(220)
        line(i*xscl, ymax, i*xscl, ymin)

    # Waagrechte Linien
    for i in range(0, (ymax-ymin)/yscl): 
        strokeWeight(1)
        stroke(220)
        line(xmin, i*yscl, xmax, i*yscl) # Zwei Linien gespiegelt an der X-Achse
        line(xmin, -i*yscl, xmax, -i*yscl)
    
    # Achsen
    strokeWeight(2)
    stroke(0)
    line(xmin, 0, xmax, 0)
    line(xmin, ymin, xmin, ymax)
    
    # Dreieckspitzen der Achsen
    fill(0)
    triangle(xmax,0,xmax-5,5,xmax-5,-5)
    triangle(0,ymin,-5,ymin+5,5,ymin+5)
    
    # Beschriftungen der Achsen
    textSize(text_groesse)
    textAlign(LEFT, TOP)
    text("Auslenkung x(t) [cm]", 20,ymin+15)
    textAlign(RIGHT, TOP)
    text("Zeit t [s]",xmax-20, 20)
    
