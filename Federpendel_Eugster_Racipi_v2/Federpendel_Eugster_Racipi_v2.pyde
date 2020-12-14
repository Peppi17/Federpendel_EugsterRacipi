from button import button
from grid import grid
from timer import timer
from federpendel import federpendel
from cosinuskurve import cosinuskurve



#Variablen fuer Schieberegler A
movingMode_A = False
pointerPos_A = 0
pointerVal_A = 1.0

#Variablen fuer Schieberegler k
movingMode_k = False
pointerPos_k = 0
pointerVal_k = 1.0

#Variablen fuer Schieberegler m
movingMode_m = False
pointerPos_m = 0
pointerVal_m = 1.0

# Definieren der Bildschirmgroesse
bild_width = 1200
bild_height = 500

# Definieren der Schriftgroesse abhaengig von der Bildschirmhoehe
text_groesse = bild_height/36 # je nach Bildschirmgroesse -> Schriftgroesse-Anpassung


# allgemeine Variablen und Variablen fuer das Zeichnen der Cosinuskurve
t = 0 # Zeit
streckung = 100 #100 = Streckung y-Achse

rand = bild_width/2-100 # Zeitpunkt, wenn die Kurve sich zu Bewegen anfangen soll.

prg_lauft = 3 # 0 = Programm laeuft nicht / 1 = Programm laeuft /
              # 2 = Programm neugestartet / 3 = Anfang des Programms

'''
# Variablen fuer physikalische Formeln
A = 1 # Amplitude
k = TWO_PI # Federstaerke
m = 1 # Masse
      # muessen gar nicht global sein. Vielleicht sind ein paar Variablen nicht global'''



##### Knoepfe (button.py) #############################################################

# Groesse Knoepfe 
knopf_laenge = bild_width/12
knopf_breite = bild_height/18
abstand_knoepfe = bild_width/90
abstand_rand_x = 20
abstand_rand_y = text_groesse*2.5 + 15 + abstand_knoepfe # vom oberen Rand -5, dann - Titelrechteck, Breite, dann - Abstand zwischen den Knoepfen

# Koordinaten Knoepfe --> eventuell unten direkt bei Knoepfe??
start_x = -bild_width/2 + abstand_rand_x
start_y = -bild_height/2 + abstand_rand_y
stop_x = -bild_width/2 + abstand_rand_x + knopf_laenge + abstand_knoepfe
stop_y = -bild_height/2 + abstand_rand_y 
reset_x = -bild_width/2 + abstand_rand_x
reset_y = -bild_height/2 + abstand_rand_y + knopf_breite + abstand_knoepfe

# Farbe und Konturfarbe der Knöpfe
start_kontur_dicke = 0
stop_kontur_dicke = 0 
reset_kontur_dicke = 0
start_kontur_farbe = 0
stop_kontur_farbe = 0
reset_kontur_farbe = 0

kontur_dicke = knopf_laenge/25

#######################################################################################

titel_laenge = 2*knopf_laenge + abstand_knoepfe
titel_breite = text_groesse*2.5 + 10

###### Raster (grid.py) ###############################################################

# Skala fuer das Raster des Graphen
xscl = 25 # 1 Schritt entspricht 1 Sekunde, wegen frameRate 25
yscl = 10
    
# X-Werte des Graphen
xmin = 0 
xmax = bild_width/2

# Y-Werte des Graphen
ymin = -bild_height/2
ymax = bild_height/2

#######################################################################################
 


balken_laenge = 60
balken_breite = 30
balken_x = -bild_width/5 
balken_y = -bild_height/2 + 5

abstand_rand_sch_x = abstand_rand_x
abstand_rand_sch_y = 50
abstand_schiebe = 40
schiebe_laenge = 150
schiebe_A_x = -bild_width/2 + abstand_rand_sch_x
schiebe_A_y = bild_height/2 - abstand_rand_sch_y
schiebe_k_x = -bild_width/2 + abstand_rand_sch_x
schiebe_k_y = bild_height/2 - abstand_rand_sch_y - abstand_schiebe
schiebe_m_x = -bild_width/2 + abstand_rand_sch_x
schiebe_m_y = bild_height/2 - abstand_rand_sch_y - 2*abstand_schiebe 


def setup():
    size(bild_width,bild_height) # Bildschirmgroesse
    frameRate(25) # Bilder pro Sekunde
    
def draw():
    global prg_lauft, t, start_kontur_dicke, stop_kontur_dicke, reset_kontur_dicke, start_kontur_farbe, stop_kontur_farbe, reset_kontur_farbe
    global movingMode_A, pointerPos_A, pointerVal_A, movingMode_k, pointerPos_k, pointerVal_k, movingMode_m, pointerPos_m, pointerVal_m  
    
    '''
    # muessen nicht abgerufen werden, da diese nur gelesen werden
    
    global schiebe_laenge, schiebe_A_x, schiebe_k_x, schiebe_A_y, schiebe_k_y
    global start_x, start_y, stop_x, stop_y, reset_x, reset_y, knopf_laenge, knopf_breite
    global xmax, xmin, ymax, ymin, xscl, yscl, rangex, rangey
    '''
    
    translate(width/2, height/2) # Verschieben des Ursprungs von oben links zur Mitte
    w = width/2
    h = height/2
    
    # Raster zeichnen
    grid(xscl, yscl, xmax, xmin, ymax, ymin, text_groesse) # Zeichnen des Rasters
    
    # Zeitangabe oben rechts
    timer(xmax, ymin, t, text_groesse)
    
    # Titel
    noStroke()
    fill(0)
    rect(-w + abstand_rand_x + 2, -h + 5 + 2, titel_laenge, titel_breite)
    fill(150)
    rect(-w + abstand_rand_x, -h + 5, titel_laenge, titel_breite)
    textAlign(CENTER, TOP)
    textSize(text_groesse*2.5)
    fill(255)
    text("Federpendel", -w + abstand_rand_x + titel_laenge/2, -h + 5)
    
    #Beschreibung
    textAlign(LEFT)
    textSize(3*text_groesse/4)
    fill(0)
    text("Diese Animation simuliert einen Federpendel ohne Daempfung.", -w+abstand_rand_x, h-10)
    
    
    # Schieberegler fuer Amplitude
    draw_ruler_A(schiebe_A_x, schiebe_A_y, schiebe_laenge)
    
    if pointerVal_A <= 0:
        A = 1 + pointerVal_A*0.01
    else:
        A = 1 + (((bild_height/2.0 - 40)/streckung) - 1)*pointerVal_A*0.01 # damit Amplitude moeglichst gross, je nach Bildschirmhoehe, werden kann
    
    fill(0)
    textAlign(LEFT)
    textSize(10)
    text("Amplitude: " + str(A*10) + " cm", schiebe_A_x, schiebe_A_y - 10)
    
    # Schieberegler fuer Federkonstante
    draw_ruler_k(schiebe_k_x, schiebe_k_y, schiebe_laenge)
    k = PI + 6*PI * pointerVal_k*0.01
    
    # Beschriftung fuer Schieberegler der Federkonstante
    if pointerVal_k <= 100/5:
        akt_k = "sehr klein"
        
    if 100/5 <= pointerVal_k <= 2*100/5:
        akt_k = "klein"    
        
    if 2*100/5 <= pointerVal_k <= 3*100/5:
        akt_k = "mittel"
        
    elif 3*100/5 <= pointerVal_k <= 4*100/5:
        akt_k = "gross"
        
    else:
        akt_k = "sehr gross"

    
    fill(0)
    textAlign(LEFT)
    textSize(10)
    text("Federkonstante: " + akt_k, schiebe_k_x, schiebe_k_y - 10)
    
    
    # Schieberegler fuer Masse
    draw_ruler_m(schiebe_m_x, schiebe_m_y, schiebe_laenge)    
    
    # Kontrolle fuer Masse
    if pointerVal_m <= 1: # Damit die Masse niemals null wird (niemals -100%), sonst gibt es bei omega eine Division durch Null -> Fehler
        pointerVal_m = 1
        m = 1 + pointerVal_m*0.01
    else:
        m = 1 + pointerVal_m*0.01
    
    # Beschriftung fuer Schieberegler der Masse
    if pointerVal_m <= 100/5:
        akt_m = "sehr leicht"
        
    if 100/5 <= pointerVal_m <= 2*100/5:
        akt_m = "leicht"    
        
    if 2*100/5 <= pointerVal_m <= 3*100/5:
        akt_m = "mittel"
        
    elif 3*100/5 <= pointerVal_m <= 4*100/5:
        akt_m = "schwer"
        
    else:
        akt_m = "sehr schwer"
        
    fill(0)
    textAlign(LEFT)
    textSize(10)
    text("Masse: " + akt_m, schiebe_m_x, schiebe_m_y - 10)
    
    # Erstellen der Variable omega fuer cosinuskurve, abhaengig von Federkonstante und Masse
    omega = sqrt(k/m)
    
    # Starten
    if  mouseButton == LEFT and start_x + w <= mouseX <= start_x + knopf_laenge + w and start_y + h <= mouseY <= start_y + knopf_breite + h : 
        prg_lauft = 1
    
    # Stoppen
    if  mouseButton == LEFT and stop_x + w <= mouseX <= stop_x + knopf_laenge + w and stop_y + h <= mouseY <= stop_y + knopf_breite + h : 
        prg_lauft = 0
        
    # Resetten
    if  mouseButton == LEFT and reset_x + w <= mouseX <= reset_x + knopf_laenge + w and reset_y + h <= mouseY <= reset_y + knopf_breite + h : 
        prg_lauft = 2

    
    if prg_lauft == 0: # Stopp, wenn Programm nicht laeuft
        cosinuskurve(A, omega, k, m, t, rand, streckung)
        federpendel(A, omega, t, streckung, balken_x, balken_y, balken_laenge, balken_breite, k, m) # Zeichnet aktuellen Stand der Federpendel und der Cosinuskurve
        
        start_kontur_dicke = 0
        stop_kontur_dicke = kontur_dicke # Stop-Knopf-Kontur wird dicker
        reset_kontur_dicke = 0
        start_kontur_farbe = 0
        stop_kontur_farbe = 255 # Stop-Knopf-Kontur wird Gelb
        reset_kontur_farbe = 0
        
    if prg_lauft == 1 : # Start, wenn Programm laeuft
        cosinuskurve(A, omega, k, m, t, rand, streckung)
        federpendel(A, omega, t, streckung, balken_x, balken_y, balken_laenge, balken_breite, k, m)
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veraenderung von 0.04 pro Bild
        # Zeichnet immer wieder Stand des Federpendels und der Cosinuskurve und erhoeht die Zeit um 0.04
        
        start_kontur_dicke = kontur_dicke # Start-Knopf-Kontur wird 2 Pixel dick
        stop_kontur_dicke = 0
        reset_kontur_dicke = 0
        start_kontur_farbe = 255 # Start-Knopf-Kontur wird Gelb
        stop_kontur_farbe = 0
        reset_kontur_farbe = 0
        
    if prg_lauft == 2: # Reset, wenn Programm neugestartet wird
            
        t = 0 # Zuruecksetzen der relevanten Variablen
        pointerPos_A = 0
        pointerVal_A = 1.0
        pointerPos_k = 0
        pointerVal_k = PI
        pointerPos_m = 0
        pointerVal_m = 1.0
            
        federpendel(A, omega, t, streckung, balken_x, balken_y, balken_laenge, balken_breite, k, m) # zeichnet Anfangsposition des Federpendels
            
        start_kontur_dicke = 0
        stop_kontur_dicke = 0
        reset_kontur_dicke = kontur_dicke # Reset-Knopf-Kontur wird 2 Pixel dick
        start_kontur_farbe = 0
        stop_kontur_farbe = 0
        reset_kontur_farbe = 255 # Reset-Knopf-Kontur wird Gelb
    

    if prg_lauft == 3: # Anfangsphase, noch kein Punkt auf Graph
        federpendel(A, omega, t, streckung, balken_x, balken_y, balken_laenge, balken_breite, k, m)
        
        start_kontur_dicke = 0 
        stop_kontur_dicke = 0
        reset_kontur_dicke = 0
        start_kontur_farbe = 0 
        stop_kontur_farbe = 0
        reset_kontur_farbe = 0
        
##### Knoepfe ###########################################################################################

    # Start-Button
    button(start_kontur_dicke, start_kontur_farbe, 0, 153, 0, start_x, start_y, knopf_laenge, knopf_breite, "Start", text_groesse)

    # Stop-Button
    button(stop_kontur_dicke, stop_kontur_farbe, 153, 0, 0, stop_x, stop_y, knopf_laenge, knopf_breite, "Stop", text_groesse)
    
    # Reset-Button
    button(reset_kontur_dicke, reset_kontur_farbe, 200, 200, 200, reset_x, reset_y, knopf_laenge, knopf_breite, "Reset", text_groesse)
    
######################################################################################################## ehemalig Funktionen   
'''
def button(kontur_dicke, farbe_linie, farbe_button1, farbe_button2, farbe_button3 , button_x, button_y, button_laenge, button_breite, name):
    strokeWeight(kontur_dicke)
    stroke(farbe_linie, farbe_linie, 0)
    fill(farbe_button1, farbe_button2, farbe_button3)
    rect(button_x, button_y, button_laenge, button_breite)
    textAlign(CENTER)
    fill(255)
    textSize(20)
    text(name, button_x + button_laenge/2 , button_y + 2*button_breite/3)
'''        


'''    
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
'''
'''        
# Cosinuskurve zeichnen
def cosinuskurve(A, omega): 
    global k, m, t, rand
    
    # Vorderster Punkt
    strokeWeight(10)
    stroke(255, 100, 0)
    if t*25 <= rand: # bis zum Rand
        point(25*t, -A*cos(omega * t)*streckung) # 25 = Streckung x-Achse
    else: # auf dem Rand
        point(rand, -A*cos(omega * t)*streckung)
    
    # kleine Punkte der Kurve
    strokeWeight(3)
    stroke(100)
    l = 0
    if t*25 <= rand: # bis zum Rand
        while l <= t :
            point(25*l, -A*cos(omega * l )*streckung)
            l = l + 0.04
    else: # Punktebewegung vor dem Rand
        for r in range(0, rand) :
            point(rand - r, -A*cos(omega*(r*0.04-t))*streckung)
'''
    
'''
# Zeitangabe oben rechts
def zeit(posX, posY):
    fill(0)
    textSize(10)
    text("Zeit: " +str(t) + " Sekunden", posX, posY)
'''

'''    
# Gewicht des Federpendels zeichnen
def federpendel(A, omega, t, streckung, objX, objY, obj_laenge, obj_breite): 
    
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
##################################################################################################3


'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''

'''angepasst auf Translation'''

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Laenge des Reglers
def draw_ruler_A(objX_vorher, objY_vorher, objLength):    
    global movingMode_A
    global pointerPos_A
    global pointerVal_A
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = 12
    if pointerPos_A == 0: 
        pointerPos_A = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(3)
    line(objX_vorher, objY_vorher, objX_vorher + objLength, objY_vorher)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX >  pointerPos_A - pointerRadius  and mouseX <  pointerPos_A + pointerRadius and mouseY > objY - pointerRadius  and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode_A = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode_A = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode_A == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos_A = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos_A = objX
            if mouseX > objX:
                pointerPos_A = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos_A-width/2, objY_vorher, pointerRadius) # angepasst wegen Translation
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal_A = int(200 / float(objLength) * (pointerPos_A - objX - objLength/2 )) # angepasst wegen Mitte
   
   
def draw_ruler_k(objX_vorher, objY_vorher, objLength):    
    global movingMode_k
    global pointerPos_k
    global pointerVal_k
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = 12
    if pointerPos_k == 0: 
        pointerPos_k = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(3)
    line(objX_vorher, objY_vorher, objX_vorher + objLength, objY_vorher)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX >  pointerPos_k - pointerRadius  and mouseX <  pointerPos_k + pointerRadius and mouseY > objY - pointerRadius  and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode_k = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode_k = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode_k == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos_k = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos_k = objX
            if mouseX > objX:
                pointerPos_k = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos_k-width/2, objY_vorher, pointerRadius) # angepasst wegen Translation
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal_k = int(100 / float(objLength) * (pointerPos_k - objX ))
  

def draw_ruler_m(objX_vorher, objY_vorher, objLength):    
    global movingMode_m
    global pointerPos_m
    global pointerVal_m
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = 12
    if pointerPos_m == 0: 
        pointerPos_m = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(3)
    line(objX_vorher, objY_vorher, objX_vorher + objLength, objY_vorher)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX >  pointerPos_m - pointerRadius  and mouseX <  pointerPos_m + pointerRadius and mouseY > objY - pointerRadius  and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode_m = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode_m = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode_m == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos_m = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos_m = objX
            if mouseX > objX:
                pointerPos_m = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos_m-width/2, objY_vorher, pointerRadius) # angepasst wegen Translation
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal_m = int(100 / float(objLength) * (pointerPos_m - objX)) 
        
    
    
