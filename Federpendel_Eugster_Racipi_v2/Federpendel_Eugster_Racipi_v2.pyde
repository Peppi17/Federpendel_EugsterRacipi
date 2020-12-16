

# Importieren der verschiedenen Funktionen aus anderen Dateien
from button import button
from cosinuskurve import cosinuskurve
from federpendel import federpendel
from grid import grid
from round import round2
from round import round1
from timer import timer

##### Verschiedene Variablen für Layout ########################################################################################

''' Diese Variablen können auf eigene Bedürfnisse angepasst werden, z.B. Bildschirmgrösse'''

# Bildschirmgroesse
bild_width = 2400
bild_height = 1200

# Schriftgroesse abhaengig von der Bildschirmhoehe
text_groesse = bild_height/48 # --> 48 Standard, umso kleiner diese Zahl, umso grösser die Schrift

##### Weitere Variablen ##########################################################################################################

# Abstand vom Rand
abstand_rand_x = 30
abstand_rand_y = 20

# Variablen fuer das Zeichnen der Cosinuskurve
t = 0 # Zeit
streckungY = 100 #Streckung y-Achse, weil Cosinus nur zwischen -1 und 1
rand = bild_width/2-text_groesse*5 # Zeitpunkt, wenn die Kurve sich zu Bewegen anfangen soll.

# Programm Modus
prg_lauft = 2 # 0 = Programm laeuft nicht 
              # 1 = Programm laeuft 
              # 2 = Programm Anfang und Reset

##### Knoepfe (button.py) ######################################################################################################

# Groesse Knoepfe 
knopf_laenge = bild_width/12
knopf_breite = bild_height/18
abstand_knoepfe = bild_width/90
titel_breite = text_groesse*2.5 + 10

# Koordinaten Knoepfe 
start_x = -bild_width/2 + abstand_rand_x
start_y = -bild_height/2 + 2*abstand_rand_y + titel_breite
stop_x = -bild_width/2 + abstand_rand_x
stop_y = start_y + knopf_breite + abstand_knoepfe
reset_x = -bild_width/2 + abstand_rand_x
reset_y = stop_y + knopf_breite + abstand_knoepfe

# Konturdicke beim Leuchten
kontur_dicke = knopf_laenge/25 

###### Raster (grid.py) ###########################################################################################################

# Skala fuer das Raster des Graphen
xscl = 25 # 1 Schritt entspricht 1 Sekunde, wegen frameRate 25
yscl = 25
    
# X-Werte des Graphen
xmin = 0 
xmax = bild_width/2

# Y-Werte des Graphen
ymin = -bild_height/2
ymax = bild_height/2
 
###### Animation des Federpendels (federpendel.py) ################################################################################

balken_laenge = bild_width/20
balken_breite = bild_height/20
balken_x = -bild_width/8 
balken_y = -bild_height/2 + abstand_rand_y

###### Variablen der Schiebergler #################################################################################################

abstand_rand_sch_x = abstand_rand_x # x-Abstand vom Rand fuer Schieberegler
abstand_rand_sch_y = 100 # y-Abstand vom Rand fuer Schieberegler
abstand_schiebe = text_groesse*4 # x-Abstand zwischen Schieberegler
schiebe_laenge = bild_width/4 # Länge des Schiereglers

# Positionen der Schieberegler
schiebe_A_x = -bild_width/2 + abstand_rand_sch_x
schiebe_A_y = bild_height/2 - abstand_rand_sch_y
schiebe_k_x = -bild_width/2 + abstand_rand_sch_x
schiebe_k_y = bild_height/2 - abstand_rand_sch_y - abstand_schiebe
schiebe_m_x = -bild_width/2 + abstand_rand_sch_x
schiebe_m_y = bild_height/2 - abstand_rand_sch_y - 2*abstand_schiebe

#Variablen fuer Schieberegler zu A
movingMode_A = False
pointerPos_A = 0
pointerVal_A = 1.0

#Variablen fuer Schieberegler zu k
movingMode_k = False
pointerPos_k = 0
pointerVal_k = 1.0

#Variablen fuer Schieberegler zu m
movingMode_m = False
pointerPos_m = 0
pointerVal_m = 1.0

###################################################################################################################################

def setup():
    size(bild_width,bild_height) # Bildschirmgroesse
    frameRate(25) # Bilder pro Sekunde
    
def draw():
    global prg_lauft, t
    global movingMode_A, pointerPos_A, pointerVal_A, movingMode_k, pointerPos_k, pointerVal_k, movingMode_m, pointerPos_m, pointerVal_m  
        
    translate(width/2, height/2) # Verschieben des Ursprungs von oben links zur Mitte
    w = width/2
    h = height/2
    
    # Raster zeichnen
    grid(xscl, yscl, xmax, xmin, ymax, ymin, text_groesse) # Zeichnen des Rasters
        
    # Titel
    textAlign(CENTER)
    textSize(text_groesse*2)
    titel = "Federpendel"
    titel_laenge = textWidth(titel) + 60
    noStroke()
    fill(50)
    rect(-w + abstand_rand_x + 4, -h + abstand_rand_y + 4, titel_laenge, titel_breite)
    fill(150)
    rect(-w + abstand_rand_x, -h + abstand_rand_y, titel_laenge, titel_breite)
    fill(255)
    text(titel, -w + abstand_rand_x + titel_laenge/2, -h + abstand_rand_y + 3*titel_breite/4)
    
    # Beschreibung
    textSize(text_groesse)
    textAlign(LEFT)
    fill(0)
    text("Diese Animation simuliert ein Federpendel ohne Daempfung.", -w + abstand_rand_x, h - abstand_rand_y) 
    
##### Schieberegler ######################################################################################################################### 
    
    # Schieberegler fuer Amplitude
    draw_ruler_A(schiebe_A_x, schiebe_A_y, schiebe_laenge)
    A = ((3.0/4.0 * h)/streckungY)*pointerVal_A*0.01 # damit Amplitude moeglichst gross, je nach Bildschirmhoehe, werden kann
    
    fill(0)
    textAlign(LEFT)
    textSize(text_groesse)
    text("Amplitude: " + str(round1(A*10)) + " cm", schiebe_A_x, schiebe_A_y - (text_groesse + 5))
      
    # Schieberegler fuer Federkonstante
    draw_ruler_k(schiebe_k_x, schiebe_k_y, schiebe_laenge)
    k = 5 + 20 * pointerVal_k*0.01
    
    fill(0)
    textAlign(LEFT)
    textSize(text_groesse)
    text("Federkonstante: " + str(round1(k)) + " N/m", schiebe_k_x, schiebe_k_y - (text_groesse + 5))
    
    # Schieberegler fuer Masse
    draw_ruler_m(schiebe_m_x, schiebe_m_y, schiebe_laenge)    
    
    # Kontrolle fuer Masse
    if pointerVal_m <= 1: # Damit die Masse niemals null wird (niemals -100%), sonst gibt es bei omega eine Division durch Null -> Fehler
        m = 1 
    else:
        m = 50 * pointerVal_m * 0.01
    
    fill(0)
    textAlign(LEFT)
    textSize(text_groesse)
    text("Masse: " + str(round1(m)) + " kg", schiebe_m_x, schiebe_m_y - (text_groesse + 5))
 
##### Anzeige der Variablen und Funktionswerte der Schwingung #############################################################################
 
    # Frequenz & Periode
    omega = sqrt(k/m) # Erstellen der Variable omega fuer cosinuskurve, abhaengig von Federkonstante und Masse
    textAlign(LEFT)
    textSize(text_groesse)
    fill(0)
    frequenz = round2(omega / TWO_PI)
    periode = round2(1/frequenz)
    text("Frequenz: " + str(frequenz) + " Hz" + "     " + "Periode: " + str(periode) + " s", abstand_rand_x, h - abstand_rand_y)
    
    # Zeitangabe
    timer(xmax, ymin, t, text_groesse)
    
    # Auslenkung
    fill(0)
    textAlign(LEFT, TOP)
    text("Auslenkung:  ", xmax-12*text_groesse, ymin+15+text_groesse+5)
    textAlign(RIGHT, TOP)
    text(str(round1(A*cos(omega * t)*10)) + " cm", xmax-20, ymin+15+text_groesse+5)
    
##### Knoepfe Modus #####################################################################################################################

# Durch Anklicken der Knöpfe wird der Programm Modus gewechselt
        
    # Starten
    if  mouseButton == LEFT and start_x + w <= mouseX <= start_x + knopf_laenge + w and start_y + h <= mouseY <= start_y + knopf_breite + h : 
        prg_lauft = 1
    
    # Stoppen
    if  mouseButton == LEFT and stop_x + w <= mouseX <= stop_x + knopf_laenge + w and stop_y + h <= mouseY <= stop_y + knopf_breite + h : 
        prg_lauft = 0
        
    # Resetten
    if  mouseButton == LEFT and reset_x + w <= mouseX <= reset_x + knopf_laenge + w and reset_y + h <= mouseY <= reset_y + knopf_breite + h : 
        prg_lauft = 2

###### Programm Modus #####################################################################################################################

    # Stopp, wenn Programm nicht laeuft
    if prg_lauft == 0: 
        
        cosinuskurve(A, omega, t, rand, streckungY)
        federpendel(A, omega, t, streckungY, balken_x, balken_y, balken_laenge, balken_breite, k, m) # Zeichnet aktuellen Stand der Federpendel und der Cosinuskurve
        
        # Variablen Knopf
        start_kontur_dicke = 0
        stop_kontur_dicke = kontur_dicke
        start_kontur_farbe = 0
        stop_kontur_farbe = 255
        
    # Start, wenn Programm laeuft        
    if prg_lauft == 1: 
        
        cosinuskurve(A, omega, t, rand, streckungY)
        federpendel(A, omega, t, streckungY, balken_x, balken_y, balken_laenge, balken_breite, k, m)
        t = t + 0.04 # 0.04 weil 1 s : 25 Bilder/s = Veraenderung von 0.04 pro Bild
        # Zeichnet immer wieder Stand des Federpendels und der Cosinuskurve und erhoeht die Zeit um 0.04
        
        #Variablen Knopf
        start_kontur_dicke = kontur_dicke
        stop_kontur_dicke = 0
        start_kontur_farbe = 255
        stop_kontur_farbe = 0
                
    # Anfang und Reset
    if prg_lauft == 2: 
        
        federpendel(A, omega, t, streckungY, balken_x, balken_y, balken_laenge, balken_breite, k, m)    
        t = 0 
        
        # Variablen Schieberegler
        pointerPos_A = 0
        pointerVal_A = 1.0
        pointerPos_k = 0
        pointerVal_k = PI
        pointerPos_m = 0
        pointerVal_m = 1.0
        
        # Variablen Knopf
        start_kontur_dicke = 0 
        stop_kontur_dicke = 0
        start_kontur_farbe = 0 
        stop_kontur_farbe = 0
        
##### Aussehen Knoepfe #####################################################################################################################################

    # Start-Button
    button(start_kontur_dicke, start_kontur_farbe, 0, 153, 0, start_x, start_y, knopf_laenge, knopf_breite, "Start", text_groesse)

    # Stop-Button
    button(stop_kontur_dicke, stop_kontur_farbe, 153, 0, 0, stop_x, stop_y, knopf_laenge, knopf_breite, "Stop", text_groesse)
    
    # Reset-Button
    button(0, 0, 200, 200, 200, reset_x, reset_y, knopf_laenge, knopf_breite, "Reset", text_groesse)
    
##### Funktion Schieberegler ##############################################################################################################################

# Optimierungsmöglichkeit: Nur eine Funktion für alle Schieberegler und als eigene Datei

'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''

'''angepasst auf Translation'''

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Laenge des Reglers

# Schieberegler für Amplitude A
def draw_ruler_A(objX_vorher, objY_vorher, objLength):    
    global movingMode_A
    global pointerPos_A
    global pointerVal_A
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = text_groesse
    if pointerPos_A == 0: 
        pointerPos_A = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(text_groesse/4)
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
    pointerVal_A = int(100 / float(objLength) * (pointerPos_A - objX))

# Schieberegler für Federstärke k
def draw_ruler_k(objX_vorher, objY_vorher, objLength):    
    global movingMode_k
    global pointerPos_k
    global pointerVal_k
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = text_groesse
    if pointerPos_k == 0: 
        pointerPos_k = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(text_groesse/4)
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
  
# Schieberegler für Masse m
def draw_ruler_m(objX_vorher, objY_vorher, objLength):    
    global movingMode_m
    global pointerPos_m
    global pointerVal_m
    
    objX =  objX_vorher + width/2 # Anpassung wegen Translation
    objY =  objY_vorher + height/2 # Anpassung wegen Translation
    
    # Schieber einstellen
    pointerRadius = text_groesse
    if pointerPos_m == 0: 
        pointerPos_m = objX+ objLength/2 # angepasst wegen Mitte
    
    # Linie zeichnen
    stroke(85)
    strokeWeight(text_groesse/4)
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
    pointerVal_m = int(100 / float(objLength) * (pointerPos_m - objX)) # Anpassung Möglichkeit Dezimalzahlen
