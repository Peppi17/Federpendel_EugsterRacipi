'''
IIIIIIIIIIIII
I
I
IIIIII
I
I  unktioniert noch nicht oder gar nicht :(  ---> Schade

'''


# -*- coding: utf-8 -*-

# angepasst auf Translation

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers

def draw_ruler(objX_vorher, objY_vorher, objLength, movingMode, pointerPos, pointerVal):    
    
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
    return(pointerVal = int(200 / float(objLength) * (pointerPos - objX - objLength/2 ))) # angepasst wegen Mitte

    
