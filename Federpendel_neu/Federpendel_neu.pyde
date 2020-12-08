
# allgemeine Variablen und Variablen für das Zeichnen der Cosinuskurve
t = 0 # Zeit
t_kurve_x = 0 # Variable für x-Koord. der Kurve, wird zurückgesetzt, wenn Punkt rechten Rand berührt.
zaehler = 0 # Zähler, jedes mal wenn der Graph den rechten Rand berührt, wirds um "rand" erhöht
rand = 24 # Zeitpunkt, wenn die Kurve wieder von Anfang an gehen soll.

prg_lauft = 3 # 0 = Programm läuft nicht / 1 = Programm läuft /
              # 2 = Programm neugestartet / 3 = Anfang des Programms

# Variablen für physikalische Formeln
A = 1 # Amplitude
k = TWO_PI # Federstärke
m = 1 # Masse


# Variablen für Knöpfe
start = 0 # Konturdicke Start-Knopf
stop = 0 # Konturdicke Stop-Knopf
reset = 0 # Konturdicke Reset-Knopf
linie_button1 = 0 # R- und G-Wert des Start-Knopfs 
linie_button2 = 0 # R- und G-Wert des Stop-Knopfs
linie_button3 = 0 # R- und G-Wert des Reset-Knopfs 

# Variablen für das Raster des Graphen
xscl = 25 # 1 Schritt entspricht 1 Sekunde, wegen frameRate 25
yscl = 20
    
# Bereich X-Werte des Graphs
xmin = 0 
xmax = 600 # halbe Bildschirmbreite : x-Streckung = Skala (t = 1 s)

# Bereich Y-Werte des Graphs
ymin = -600/2
ymax = 600/2 # halbe Bildschirmhöhe : y-Streckung = Skala (x = 10 cm)
    
# Bereich Graph
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    size(1200,600) # Bildschirmgrösse
    frameRate(25) # Bilder pro Sekunde
    
def draw():
    global prg_lauft, t, t_kurve_x, t_kurve_y, start, stop, reset, linie_button1, linie_button2, linie_button3, xmax, xmin, ymax, ymin, xscl, yscl, rangex, rangey
    
    translate(width/2, height/2) # Verschieben des Ursprungs von oben links zur Mitte
    grid() # Zeichnen des Rasters
    zeit() # Zeitangabe oben rechts
    
    # Starten
    if  mouseButton == LEFT and 10 <= mouseX <= 90 and 10 <= mouseY <= 40 : 
        prg_lauft = 1
        start = 2 # Start-Knopf-Kontur wird 2 Pixel dick
        stop = 0
        reset = 0
        linie_button1 = 255 # Start-Knopf-Kontur wird Gelb
        linie_button2 = 0
        linie_button3 = 0
    
    # Stoppen
    if  mouseButton == LEFT and 100 <= mouseX <= 180 and 10 <= mouseY <= 40 : 
        prg_lauft = 0
        start = 0
        stop = 2 # Stop-Knopf-Kontur wird 2 Pixel dick
        reset = 0
        linie_button1 = 0
        linie_button2 = 255 # Stop-Knopf-Kontur wird Gelb
        linie_button3 = 0
        
    # Resetten
    if  mouseButton == LEFT and 10 <= mouseX <= 90 and 50 <= mouseY <= 80 : 
        prg_lauft = 2
        start = 0
        stop = 0
        reset = 2 # Reset-Knopf-Kontur wird 2 Pixel dick
        linie_button1 = 0
        linie_button2 = 0
        linie_button3 = 255 # Reset-Knopf-Kontur wird Gelb
    
    if prg_lauft == 0: # Stopp, wenn Programm nicht läuft
        cosinuskurve()
        federpendel() # Zeichnet aktuellen Stand der Federpendel und der Cosinuskurve
        
    if prg_lauft == 1 : # Start, wenn Programm läuft
        cosinuskurve()
        federpendel()
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
        t_kurve_x = t_kurve_x + 0.04
        # Zeichnet immer wieder Stand der Federpendel und der Cosinuskurve und erhöht die Zeit um 0.04
    
    if prg_lauft == 2: # Reset, wenn Programm neugestartet wird
        t = 0 # Zurücksetzen der relevanten Variablen
        t_kurve_x = 0 
        zaehler = 0 

        federpendel() # zeichnet Anfangsposition des Federpendels

    if prg_lauft == 3: # Anfangsphase, noch kein Punkt auf Graph
        federpendel()

#Knöpfe

    # Start-Button
    strokeWeight(start)
    stroke(linie_button1, linie_button1, 0)
    fill(0,153,0)
    rect(-590,-290, 80, 30)
    fill(255)
    textSize(20)
    text("Start",-575,-270)

    # Stop-Button
    strokeWeight(stop)
    stroke(linie_button2, linie_button2, 0)
    fill(153,0,0)
    rect(-500,-290, 80, 30)
    fill(255)
    textSize(20)
    text("Stop",-485,-270)
    
    # Reset-Button
    strokeWeight(reset)
    stroke(linie_button3, linie_button3, 0)
    fill(200)
    rect(-590,-250, 80, 30)
    fill(255)
    textSize(20)
    text("Reset",-580,-230)
    
    
# Kariertes Raster
def grid():
    global xscl, yscl, xmax, xmin, ymax, ymin, rangex, rangey
    background(255) # weisser Hintergrund

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
    textSize(10)
    text("Zeit t",540,15) # Text "Zeit t" zur X-Achse
    text("Amplitude A",5,-280) # Text "Amplitude A" zur Y-Achse
    
# Cosinuskurve zeichnen
def cosinuskurve(): 
    global A, k, m, t, t_kurve_x, zaehler, rand
    
    omega = sqrt(k/m)
    
    # Kontrolle, ob Kurve den rechten Rand berührt hat
    if t_kurve_x >= rand :
        t_kurve_x = 0
        zaehler = zaehler + rand
        
    # neuester Punkt auf dem Graph
    strokeWeight(10)
    stroke(255, 100, 0)        
    point(25*t_kurve_x, -A*cos(omega * t)*200) # 25 = Streckung x-Achse, 200 = Streckung y-Achse
    
    # Alle anderen Punkte davor zeichnen
    strokeWeight(3)
    stroke(100)
    #punkt_max = int(t_kurve_x/0.04) # Vorbereitung für for-Schleife: keine floats
    
    l = 0
    while l <= t_kurve_x :
        point(25*l, -A*cos(omega*(zaehler + l) )*200)
        l = l + 0.04
    
    #for l in range(0, punkt_max) :
        #point(l, -A*cos(omega*(zaehler + (l*0.04)))*200)

    

# Zeitangabe oben rechts
def zeit():
    fill(0)
    textSize(10)
    text(t, 480, -285)
    text("Sekunden", 530, -285)

    
# Gewicht des Federpendels zeichnen
def federpendel(): 
    omega = sqrt(k/m)
    
    noStroke()
    fill(200)
    rect(-330,-300,60,30) # Linie("Feder") und Balken oben, an dem der Ball angemacht ist
    
    strokeWeight(2)
    stroke(0)
    line(-300,-270,-300,-A*cos(omega*t)*200)
    strokeWeight(25)
    stroke(255, 100, 0)
    point(-300, -A*cos(omega*t)*200) # Kreieren der neuen Zeichnung (Ball und Linie)
    
