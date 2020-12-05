
# Variablen
t = 0 # Zeit
A = 1 # Amplitude

prg_lauft = 0 # 1 = Programm lauft / 0 = Programm lauft nicht


def setup():
    background(255)
    size(1200,600) #voller Bildschirm
    frameRate(25) # Bilder pro Sekunde

    
    grid()
    
    
def draw():
    translate(width/2, height/2)
    global prg_lauft
    
    if  mouseButton == LEFT and 10 <= mouseX <= 90 and 10 <= mouseY <= 40 :
        prg_lauft = 1
        
    if  mouseButton == LEFT and 100 <= mouseX <= 180 and 10 <= mouseY <= 40 :
        prg_lauft = 0
    
    if prg_lauft == 1 :
        # Cosinus Kurve
        global A, t
        strokeWeight(5)
        stroke(0)
        point(25*t, -A*cos(t)*200) # 25 = Streckung x-Achse, 100 = Streckung y-Achse
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
            
        
    
    # Start-Button
    noStroke()
    fill(0,153,0)
    rect(-590,-290, 80, 30)
    fill(255)
    text("Start",-575,-270)
    textSize(20)
    
    # Stop-Button
    noStroke()
    fill(153,0,0)
    rect(-500,-290, 80, 30)
    fill(255)
    text("Stop",-485,-270)
    textSize(20)
    
# Kariertes Raster
def grid():
    xscl = 25 
    yscl = 20
    
    # Bereich X-Werte
    xmin = 0 
    xmax = width # halbe Bildschirmbreite : x-Streckung = Skala (t = 1 s)

    # Bereich Y-Werte
    ymin = -height/2
    ymax = height/2 # halbe Bildschirmhöhe : y-Streckung = Skala (x = 10 cm)
    
    # Bereich Graph
    rangex = xmax - xmin
    rangey = ymax - ymin
    
    translate(width/2, height/2)
    
    for i in range(0, rangex/xscl): # Senkrechte Linien
        strokeWeight(1)
        stroke(220)
        line(i*xscl, ymax, i*xscl, ymin)

    for i in range(0, rangey/yscl): # Waagrechte Linien
        strokeWeight(1)
        stroke(220)
        line(xmin, i*yscl, xmax, i*yscl) # Zwei Linien gespiegelt an der X-Achse
        line(xmin, -i*yscl, xmax, -i*yscl)
    
    strokeWeight(2)
    stroke(0)
    line(xmin, 0, xmax, 0) # X-Achse
    line(xmin, ymin, xmin, ymax) # Y-Achse
    fill(0)
    triangle(600,0,600-5,5,600-5,-5)
    triangle(0,-300,-5,-295,5,-295)
    text("Zeit t",540,15)
    text("Amplitude A",5,-280)
    textSize(10)




      
