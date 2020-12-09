
movingMode1 = False
pointerPos1 = 0
pointerValA = 1.0
pointerPos2 = 0
movingMode2 = False
pointerValk = 1.0
pointerPos3 = 0
pointerValm = 1.0

# allgemeine Variablen und Variablen für das Zeichnen der Cosinuskurve
t = 0 # Zeit
streckung = 100 #100 = Streckung y-Achse

rand = 19 # Zeitpunkt, wenn die Kurve sich zu Bewegen anfangen soll.

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

bild_width = 1000
bild_height = 500
abstand_rand = 10
abstand_knoepfe = 10

#Koordinaten Knöpfe
knopf_laenge = 80
knopf_breite = 30
start_x = -bild_width/2 + abstand_rand
start_y = -bild_height/2 + abstand_rand
stop_x = -bild_width/2 + abstand_rand + knopf_laenge + abstand_knoepfe
stop_y = -bild_height/2 + abstand_rand 
reset_x = -bild_width/2 + abstand_rand
reset_y = -bild_height/2 + abstand_rand + knopf_breite + abstand_knoepfe
 
balken_laenge = 60
balken_breite = 30
balken_x = -bild_width/5
balken_y = -bild_height/2

abstand_rand_sch_x = 20
abstand_rand_sch_y = 50
abstand_schiebe = 40
schiebe_laenge = 150
schiebe1_x = -bild_width/2 + abstand_rand_sch_x
schiebe1_y = bild_height/2 - abstand_rand_sch_y
schiebe2_x = -bild_width/2 + abstand_rand_sch_x
schiebe2_y = bild_height/2 - abstand_rand_sch_y - abstand_schiebe 

zeit_x = bild_width/2 - 120
zeit_y = -bild_height/2 + 15


# Variablen für das Raster des Graphen
xscl = 25 # 1 Schritt entspricht 1 Sekunde, wegen frameRate 25
yscl = 20
    
# Bereich X-Werte des Graphs
xmin = 0 
xmax = bild_width/2 # halbe Bildschirmbreite : x-Streckung = Skala (t = 1 s)

# Bereich Y-Werte des Graphs
ymin = -bild_height/2
ymax = bild_height/2 # halbe Bildschirmhöhe : y-Streckung = Skala (x = 10 cm)
    
# Bereich Graph
rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    size(bild_width,bild_height) # Bildschirmgrösse
    frameRate(25) # Bilder pro Sekunde
    
def draw():
    global prg_lauft, t, start, stop, reset, linie_button1, linie_button2, linie_button3
    global xmax, xmin, ymax, ymin, xscl, yscl, rangex, rangey, pointerVal, pointerPos
    global start_x, start_y, stop_x, stop_y, reset_x, reset_y, knopf_laenge, knopf_breite
    global schiebe_laenge, schiebe1_x, schiebe2_x, schiebe1_y, schiebe2_y, movingMode1, pointerPos1, pointerValA, movingMode2, pointerPos2, pointerValk  
    
    translate(width/2, height/2) # Verschieben des Ursprungs von oben links zur Mitte
    w = width/2
    h = height/2
    
    grid(xscl, yscl, xmax, xmin, ymax, ymin, rangex, rangey) # Zeichnen des Rasters
    zeit(zeit_x, zeit_y) # Zeitangabe oben rechts
    
    # Schieberegler für Amplitude
    draw_ruler(schiebe1_x, schiebe1_y, schiebe_laenge, pointerPos1, pointerValA, movingMode1)
    draw_ruler(schiebe2_x, schiebe2_y, schiebe_laenge, pointerPos2, pointerValk, movingMode2)
    A = 1 + pointerValA*0.01
    fill(0)
    textAlign(LEFT)
    textSize(10)
    text("Amplitude: " + str(A*10) + " cm", schiebe1_x, schiebe1_y - 10)
    text("Federstärke: " + str(pointerValk) + " EINHEIT", schiebe2_x, schiebe2_y - 10)
    
    omega = sqrt(k/m)
    
    # Starten
    if  mouseButton == LEFT and start_x + w <= mouseX <= start_x + knopf_laenge + w and start_y + h <= mouseY <= start_y + knopf_breite + h : 
        prg_lauft = 1
        start = 2 # Start-Knopf-Kontur wird 2 Pixel dick
        stop = 0
        reset = 0
        linie_button1 = 255 # Start-Knopf-Kontur wird Gelb
        linie_button2 = 0
        linie_button3 = 0
    
    # Stoppen
    if  mouseButton == LEFT and stop_x + w <= mouseX <= stop_x + knopf_laenge + w and stop_y + h <= mouseY <= stop_y + knopf_breite + h : 
        prg_lauft = 0
        start = 0
        stop = 2 # Stop-Knopf-Kontur wird 2 Pixel dick
        reset = 0
        linie_button1 = 0
        linie_button2 = 255 # Stop-Knopf-Kontur wird Gelb
        linie_button3 = 0
        
    # Resetten
    if  mouseButton == LEFT and reset_x + w <= mouseX <= reset_x + knopf_laenge + w and reset_y + h <= mouseY <= reset_y + knopf_breite + h : 
        prg_lauft = 2
        start = 0
        stop = 0
        reset = 2 # Reset-Knopf-Kontur wird 2 Pixel dick
        linie_button1 = 0
        linie_button2 = 0
        linie_button3 = 255 # Reset-Knopf-Kontur wird Gelb
    
    if prg_lauft == 0: # Stopp, wenn Programm nicht läuft
        cosinuskurve(A, omega)
        federpendel(A, omega, streckung, balken_x, balken_y, balken_laenge, balken_breite) # Zeichnet aktuellen Stand der Federpendel und der Cosinuskurve
        
    if prg_lauft == 1 : # Start, wenn Programm läuft
        cosinuskurve(A, omega)
        federpendel(A, omega, streckung, balken_x, balken_y, balken_laenge, balken_breite)
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
        # Zeichnet immer wieder Stand der Federpendel und der Cosinuskurve und erhöht die Zeit um 0.04
        # 0.04 weil 1 s : 25 Bilder/s = Veränderung von 0.04 pro Bild
        
    if prg_lauft == 2: # Reset, wenn Programm neugestartet wird
        t = 0 # Zurücksetzen der relevanten Variablen
        pointerPos = 0
        pointerVal = 1.0

        federpendel(A, omega, streckung, balken_x, balken_y, balken_laenge, balken_breite) # zeichnet Anfangsposition des Federpendels

    if prg_lauft == 3: # Anfangsphase, noch kein Punkt auf Graph
        federpendel(A, omega, streckung, balken_x, balken_y, balken_laenge, balken_breite)

#Knöpfe

    # Start-Button
    button(start, linie_button1, 0, 153, 0, start_x, start_y, knopf_laenge, knopf_breite, "Start")

    # Stop-Button
    button(stop, linie_button2, 153, 0, 0, stop_x, stop_y, knopf_laenge, knopf_breite, "Stop")
    
    # Reset-Button
    button(reset, linie_button3, 200, 200, 200, reset_x, reset_y, knopf_laenge, knopf_breite, "Reset")
    

def button(kontur_dicke, farbe_linie, farbe_button1, farbe_button2, farbe_button3 , button_x, button_y, button_laenge, button_breite, name):
    strokeWeight(kontur_dicke)
    stroke(farbe_linie, farbe_linie, 0)
    fill(farbe_button1, farbe_button2, farbe_button3)
    rect(button_x, button_y, button_laenge, button_breite)
    textAlign(CENTER)
    fill(255)
    textSize(20)
    text(name, button_x + button_laenge/2 , button_y + 2*button_breite/3)
        
    
# Kariertes Raster
def grid(xscl, yscl, xmax, xmin, ymax, ymin, rangex, rangey):
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
    triangle(xmax,0,xmax-5,5,xmax-5,-5) # Spitze X-Achse
    triangle(0,ymin,-5,ymin+5,5,ymin+5) # Spitze  Y-Achse
    textSize(10)
    textAlign(LEFT)
    text("Zeit t",xmax-50,15) # Text "Zeit t" zur X-Achse
    text("Amplitude A",5,ymin+20) # Text "Amplitude A" zur Y-Achse

        
# Cosinuskurve zeichnen
def cosinuskurve(A, omega): 
    global k, m, t, rand
    
    # Vorderster Punkt
    strokeWeight(10)
    stroke(255, 100, 0)
    if t <= rand: # bis zum Rand
        point(25*t, -A*cos(omega * t)*streckung) # 25 = Streckung x-Achse
    else: # auf dem Rand
        point(25*rand, -A*cos(omega * t)*streckung)
    
    # kleine Punkte der Kurve
    strokeWeight(3)
    stroke(100)
    l = 0
    if t <= rand: # bis zum Rand
        while l <= t :
            point(25*l, -A*cos(omega * l )*streckung)
            l = l + 0.04
    else: # Punktebewegung vor dem Rand
        for r in range(0, 25*rand) :
            point(25*rand - r, -A*cos(omega*(r*0.04-t))*streckung)
    

# Zeitangabe oben rechts
def zeit(posX, posY):
    fill(0)
    textSize(10)
    text("Zeit: " +str(t) + " Sekunden", posX, posY)

    
# Gewicht des Federpendels zeichnen
def federpendel(A, omega, streckung, objX, objY, obj_laenge, obj_breite): 
    
    noStroke()
    fill(200)
    rect(objX - obj_laenge/2, objY, obj_laenge, obj_breite) # Linie("Feder") und Balken oben, an dem der Ball angemacht ist
    #rect(-330,-300,60,30)
    
    strokeWeight(2)
    stroke(0)
    line(objX, objY + obj_breite, objX,-A*cos(omega*t)*streckung)
    strokeWeight(25)
    stroke(255, 100, 0)
    point(objX, -A*cos(omega*t)*streckung) # Kreieren der neuen Zeichnung (Ball und Linie)
    

'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''

'''angepasst auf Translation'''

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX_vorher, objY_vorher, objLength, pointerPos, PointerVal, movingMode):
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = 12
    if pointerPos == 0: 
        pointerPos = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    fill(85)
    strokeWeight(3)
    line(objX_vorher, objY_vorher, objX_vorher + objLength, objY_vorher)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX >  pointerPos - pointerRadius  and mouseX <  pointerPos + pointerRadius and mouseY > objY - pointerRadius  and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos-width/2, objY_vorher, pointerRadius) # angepasst wegen Translation
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(200 / float(objLength) * (pointerPos - objX - objLength/2 )) # angepasst wegen Mitte
    
    return movingMode, pointerPos, PointerVal
