
# Variablen
t = 0 # Zeit
A = 1 # Amplitude

prg_lauft = 0 # 1 = Programm läuft / 0 = Programm läuft nicht
start = 0
stop = 0
linie_button1 = 0
linie_button2 = 0

def setup():
    background(255)
    size(1200,600) # Bildschirmgrösse
    frameRate(25) # Bilder pro Sekunde
    grid()
    
    
def draw():
    translate(width/2, height/2)
    global prg_lauft, t, start, stop, linie_button1, linie_button2
    
    if  mouseButton == LEFT and 10 <= mouseX <= 90 and 10 <= mouseY <= 40 :
        prg_lauft = 1
        start = 2
        stop = 0
        linie_button1 = 255
        linie_button2 = 0
        
    if  mouseButton == LEFT and 100 <= mouseX <= 180 and 10 <= mouseY <= 40 :
        prg_lauft = 0
        start = 0
        stop = 2
        linie_button1 = 0
        linie_button2 = 255
    
    if prg_lauft == 1 :
        cosinuskurve()
        federpendel()
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
    
    # Start-Button
    strokeWeight(start)
    stroke(linie_button1, linie_button1, 0)
    fill(0,153,0)
    rect(-590,-290, 80, 30)
    fill(255)
    text("Start",-575,-270)
    textSize(20)
    
    # Stop-Button
    strokeWeight(stop)
    stroke(linie_button2, linie_button2, 0)
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
    triangle(600,0,600-5,5,600-5,-5) # Spitze X-Achse
    triangle(0,-300,-5,-295,5,-295) # Spitze  Y-Achse
    text("Zeit t",540,15) # Text "Zeit t" zur X-Achse
    text("Amplitude A",5,-280) # Text "Amplitude A" zur Y-Achse
    textSize(10)

def cosinuskurve(): # Cosinuskurve zeichnen
    global A
    strokeWeight(5)
    stroke(0)
    point(25*t, -A*cos(t)*200) # 25 = Streckung x-Achse, 100 = Streckung y-Achse
    

def federpendel(): # Gewicht des Federpendels zeichnen
    noStroke()
    fill(200)
    rect(-330,-300,60,30)
    
    strokeWeight(2)
    stroke(255)
    line(-300,-270,-300,-A*cos(t-0.04)*200)
    strokeWeight(30)
    stroke(255, 255, 255)
    point(-300, -A*cos(t-0.04)*200) # vorherigen Ball löschen (weiss machen)
    
    strokeWeight(2)
    stroke(0)
    line(-300,-270,-300,-A*cos(t)*200)
    strokeWeight(20)
    stroke(255, 100, 0)
    point(-300, -A*cos(t)*200) # Kreieren des neuen Balls
    
